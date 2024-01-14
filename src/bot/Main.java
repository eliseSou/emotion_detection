package bot;

import com.fasterxml.jackson.core.exc.StreamReadException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.DatabindException;
import com.fasterxml.jackson.databind.ObjectMapper;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.utils.cache.CacheFlag;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();
        try {
            Map<String, Object> config = objectMapper.readValue(new FileReader("./src/bot/config.json"), new TypeReference<Map<String, Object>>() {
            });
            String token = (String)config.get("token");
            JDABuilder builder = JDABuilder.createDefault(token);


            // Disable parts of the cache
            builder.disableCache(CacheFlag.MEMBER_OVERRIDES);
            // Enable the bulk delete event
            builder.setBulkDeleteSplittingEnabled(false);
            // Set activity (like "playing Something")
            builder.setActivity(Activity.customStatus("aaaaa"));

            builder.enableIntents(GatewayIntent.MESSAGE_CONTENT, GatewayIntent.GUILD_MESSAGES);

            builder.addEventListeners(new BotCommands());

            JDA jda = builder.build();

            jda.upsertCommand("ping","Répond pong.").setGuildOnly(false).queue();
            jda.upsertCommand("join","Rejoint votre vocal et vous écoute").setGuildOnly(true).queue();
            jda.upsertCommand("leave","...").setGuildOnly(true).queue();
            ///jda.upsertCommand("join","Rejoint votre vocal et vous écoute").setGuildOnly(true).queue();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }



    }


}