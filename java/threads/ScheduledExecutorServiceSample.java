public class ScheduledExecutorServiceSample {

        static int MAX_COUNT = 6;
        static volatile int  counter = 0;

        public static void main(String[] args) {
                final ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
                ArrayList<ScheduledFuture<?>> futures = new ArrayList<>();
                final Runnable runnable = new Runnable() {
                        @Override
                        public void run() {
                                System.out.println("Runnuble: "+counter++);
                        }
                };

                while(true){

                        //This avoid counter to go too fast
                        try {
                                Thread.sleep(1200);
                        } catch (InterruptedException e) {
                                e.printStackTrace();
                        }

                        if (counter > MAX_COUNT - 1){
                                // we cancel everything
                                for(ScheduledFuture<?> future : futures)
                                        if(!future.isCancelled())
                                                future.cancel(true);
                                scheduler.shutdown();
                                break;
                        }else{		
                                //we put the future in a list
                                futures.add(scheduler.scheduleAtFixedRate(runnable, 500, 1000, TimeUnit.MILLISECONDS));
                        }


                }

        }

}
