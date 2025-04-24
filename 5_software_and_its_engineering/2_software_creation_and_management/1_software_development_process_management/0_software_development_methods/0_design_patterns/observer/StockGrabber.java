package Observer;

import java.util.ArrayList;

/**
 * Created by Praise on 2016/11/26.
 */
//java.util.Observable
public class StockGrabber implements Subject {

    private ArrayList<Observer> observers;

    private double ibmPrice;
    private double aaplPrice;
    private double googPrice;

    public StockGrabber() {

        observers = new ArrayList<Observer>();
    }

    public void setIbmPrice(double ibmPrice) {
        this.ibmPrice = ibmPrice;
        notiyObserver(); // I don't like this, even if one changes, we resend all of them??
    }

    public void setAaplPrice(double aaplPrice) {
        this.aaplPrice = aaplPrice;
        notiyObserver();
    }

    public void setGoogPrice(double googPrice) {
        this.googPrice = googPrice;
        notiyObserver();
    }

    @Override
    public void register(Observer observer) {

        observers.add(observer);
    }

    @Override
    public void unregister(Observer observer) {

        int observerIndex = observers.indexOf(observer);
        System.out.println("Observer" + observerIndex + 1 + "deleted");
        observers.remove(observerIndex);
    }

    @Override
    public void notiyObserver() {
        for (Observer observer : observers) {
            observer.update(ibmPrice, aaplPrice, googPrice);
        }

    }
}
