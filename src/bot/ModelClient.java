package bot;

import java.io.*;
import java.net.Socket;

public class ModelClient {
    // The remote process will run on localhost and listen on
    // port 65432.
    public static final String REMOTE_HOST = "127.0.0.1";
    public static final int REMOTE_PORT = 65432;

    public static final BufferedWriter sockOut;

    static {
        // Make a TCP connection to the remote process.
        Socket socket = null;
        try {
            socket = new Socket(REMOTE_HOST, REMOTE_PORT);

            // Build BufferedWriter and BufferedReader from the socket so we
            // can do two-way text-based I/O.
            sockOut = new BufferedWriter(
                    new OutputStreamWriter(socket.getOutputStream()));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    static void sendPingToServer(String filePath) throws IOException {
        sockOut.write(filePath, 0, filePath.length());
        sockOut.newLine();
        sockOut.flush();
    }
}
