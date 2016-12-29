public class ShutDownHook {
    static class Message extends Thread {

        public void run() {
            try {

                while(true)
                {
                    System.out.println("Hello World from run");

                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        try {
            //when the main terminate the Message Thread will be triggered    
            Runtime.getRuntime().addShutdownHook(new Message());
            while(true)
            {
                System.out.println("Hello World");
                Thread.sleep(100);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
