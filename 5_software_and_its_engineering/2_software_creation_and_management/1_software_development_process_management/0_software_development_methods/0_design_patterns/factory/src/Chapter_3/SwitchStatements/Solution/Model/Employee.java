package Chapter_3.SwitchStatements.Solution.Model;

import Chapter_3.SwitchStatements.CommonModel.Money;

/**
 * Created by Praise on 2016/08/21.
 */

//Defines employee behaviour once
public abstract class Employee {
    public abstract Boolean isPayDay();
    public abstract Money calculatePay();
    public abstract void deliverPay(Money e);
}
