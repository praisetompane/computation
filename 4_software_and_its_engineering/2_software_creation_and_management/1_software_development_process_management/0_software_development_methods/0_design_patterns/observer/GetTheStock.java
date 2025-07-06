package Observer;

import java.text.DecimalFormat;

/**
 * Created by Praise on 2016/11/26.
 */

public class GetTheStock implements Runnable {

    private String stock;
    private double price;
    private int startTime;

    private Subject stockGrabber;

    // Could be an external stock price provider (INET, Bloomberg)
    public GetTheStock(Subject stockGrabber, int startTime, String stock, double price) {
        this.stockGrabber = stockGrabber;
        this.stock = stock;
        this.price = price;
        this.startTime = startTime;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 20; i++) {
            try {
                Thread.sleep(startTime);
            } catch (InterruptedException e) {
            }

            double randNum = (Math.random() * (.06 - .03));

            DecimalFormat df = new DecimalFormat("#.##");

            if (stock == "IBM") ((StockGrabber) stockGrabber).setIbmPrice(price);
            if (stock == "AAPL") ((StockGrabber) stockGrabber).setAaplPrice(price);
            if (stock == "GOOG") ((StockGrabber) stockGrabber).setGoogPrice(price);

            System.out.println(stock + ": " + df.format((price + randNum)) + " " + df.format(randNum));
            System.out.println();
        }

    }
}
