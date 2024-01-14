package bot;

import net.dv8tion.jda.api.AccountType;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.entities.Activity;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.entities.emoji.Emoji;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.events.interaction.component.ButtonInteractionEvent;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.interactions.components.buttons.Button;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.utils.cache.CacheFlag;

public class Main {
    public static void main(String[] args) {
        JDABuilder builder = JDABuilder.createDefault("MTE4MTU5ODIyMDc4NzM5NjczMA.GN91rh.kCv7xy79H8Fg4lwz6__6_5rtAyyYYfSnblhdqQ");

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

    }


}