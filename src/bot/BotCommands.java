package bot;

import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.net.*;
import java.util.*;

public class BotCommands extends ListenerAdapter {

    private Map<String,Audio> audios = new HashMap();

    static private  String publicIp;
    static {
        try(final DatagramSocket socket = new DatagramSocket()){
            socket.connect(InetAddress.getByName("8.8.8.8"), 10002);
            publicIp = socket.getLocalAddress().getHostAddress();
        } catch (SocketException | UnknownHostException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void onSlashCommandInteraction(SlashCommandInteractionEvent event) {

        Guild g = event.getGuild();
        String guildId = g.getId();

        String response;

        switch (event.getName()){
            case "ping":
                response = "PONG";
                break;
            case "join":
                if(!audios.containsKey(guildId)){
                    audios.put(guildId,new Audio(g,event.getUser()));
                }
                Member member = event.getMember();
                assert member != null;
                response = audios.get(guildId).connectToUserChannel(member, publicIp) ? "Joining voice channel..." : "You are not connected to any voice channel...";

                break;
            case "leave":
                Audio audio = audios.get(guildId);
                if(audio != null){
                    audio.disconnect();
                }
                response = "Leaving voice channel...";
                break;

            default :
                response = "Commande inconnue";
        }

        event.reply(response).setEphemeral(true).queue();
    }

}
