package Observer;

/**
 * Created by Praise on 2016/11/26.
 */
public class StockObserver implements Observer {

    private static int observerIdTracker = 0;
    private double ibmPrice;
    private double aaplPrice;
    private double googPrice;
    private int observerID;

    private Subject stockGrabber;

    public StockObserver(Subject stockGrabber) {
        this.stockGrabber = stockGrabber;
        this.observerID = ++observerIdTracker;

        System.out.println("New Observer " +  this.observerID);
        stockGrabber.register(this);

    }

    @Override
    public void update(double ibmPrice, double aapplPrice, double googPrice) {
        this.ibmPrice = ibmPrice;
        this.aaplPrice = aapplPrice;
        this.googPrice = googPrice;

        System.out.println("OberverID: " + observerID + " has been updated!");
        printPrices();
    }

    public void printPrices(){
        System.out.println("\nIBM: " + ibmPrice + "\nAPPLE: " + aaplPrice
                + "\nGOOG: " + googPrice + "\n");
    }
}
