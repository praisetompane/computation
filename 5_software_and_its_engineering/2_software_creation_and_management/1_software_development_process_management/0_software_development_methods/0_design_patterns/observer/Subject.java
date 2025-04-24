package Observer;

/**
 * Created by Praise on 2016/11/26.
 */
//java.util.Observable
public interface Subject {

    public void register(Observer o);
    public void unregister(Observer o);
    public void notiyObserver(); //update
}
