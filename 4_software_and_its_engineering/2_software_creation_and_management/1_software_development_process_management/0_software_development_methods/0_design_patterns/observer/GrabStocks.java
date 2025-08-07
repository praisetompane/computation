package Observer;

/**
 * Created by Praise on 2016/11/26.
 */
public class GrabStocks {
    public static void main(String[] args) {
        StockGrabber stockGrabber = new StockGrabber();


        /* Why does my observer need to know the Subject?
           So that it can register itself as a Subscriber??
         */
        StockObserver observer1 = new StockObserver(stockGrabber);



        //State change
        //Each individual change calls each observer's update method
        stockGrabber.setAaplPrice(197.00);
        stockGrabber.setIbmPrice(677.60);
        stockGrabber.setGoogPrice(676.40);


        StockObserver observer2 = new StockObserver(stockGrabber);
        //State change
        stockGrabber.setAaplPrice(197.00);
        stockGrabber.setIbmPrice(677.60);
        stockGrabber.setGoogPrice(676.40);


        Runnable getIBM = new GetTheStock(stockGrabber, 2 , "IBM", 197.00);
        Runnable getAPPL = new GetTheStock(stockGrabber, 2 , "APPL", 677.60);
        Runnable getGOOG = new GetTheStock(stockGrabber, 2 , "GOOG", 676.40);

        new Thread(getIBM).start();
        new Thread(getAPPL).start();
        new Thread(getGOOG).start();
    }
}
