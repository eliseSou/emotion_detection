package bot;

import net.dv8tion.jda.api.audio.AudioReceiveHandler;
import net.dv8tion.jda.api.audio.CombinedAudio;
import net.dv8tion.jda.api.audio.UserAudio;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.channel.concrete.VoiceChannel;
import net.dv8tion.jda.api.managers.AudioManager;

import javax.sound.sampled.*;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Audio implements AudioReceiveHandler {
    private final AudioManager audioManager;
    private final List<byte[]> audio = new ArrayList<>();

    public Audio(Guild g){
        this.audioManager = g.getAudioManager();
        this.audioManager.setSelfMuted(true);
        this.audioManager.setReceivingHandler(this);
    }

    @Override
    public boolean canReceiveCombined() {
        return true;
    }

    @Override
    public boolean canReceiveUser() {
        return false;
    }

    @Override
    public void handleCombinedAudio(CombinedAudio combinedAudio){
        try {
            audio.add(combinedAudio.getAudioData(1));
            if(audio.size() >= 200){
                save();
            }
        }catch (OutOfMemoryError e) {
            //close connection
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public boolean connectToUserChannel(Member member, String publicIp){
        if(member.getVoiceState() == null || member.getVoiceState().getChannel() == null ){
            return false;
        }
        VoiceChannel voiceChannel = member.getVoiceState().getChannel().asVoiceChannel();
        this.audioManager.openAudioConnection(voiceChannel);

        String addr = "http://"+publicIp+":3002";
        member.getVoiceState().getChannel().asGuildMessageChannel().sendMessage(addr).queue();

        return true;
    }


    public void disconnect(){
        this.audioManager.closeAudioConnection();
    }

    public void save() throws IOException {
        List<byte[]> copy = List.copyOf(this.audio);
        this.audio.clear();
        String fileName = "./discordRecord.wav";

        int size=0;
        for (byte[] bs : copy) {
            size+=bs.length;
        }

        byte[] decodedData = new byte[size];
        int i=0;
        for (byte[] bs : copy) {
            for (byte b : bs) {
                decodedData[i++] = b;
            }
        }


        AudioFormat audioFormat = new AudioFormat(48000.0f, 16, 2, true, true);
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(decodedData);
        AudioInputStream audioInputStream = new AudioInputStream(byteArrayInputStream, audioFormat,
                decodedData.length / audioFormat.getFrameSize());

        File audioFile = new File(fileName);
        AudioSystem.write(audioInputStream, AudioFileFormat.Type.WAVE, audioFile);

        System.out.println("Audio enregistré avec succès : " + fileName);

        ModelClient.sendPingToServer(audioFile.getAbsolutePath());
    }

}
