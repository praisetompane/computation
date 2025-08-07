package Chapter_3.SwitchStatements.Solution.Model;

import Chapter_3.SwitchStatements.CommonModel.Money;

/**
 * Created by Praise on 2016/08/21.
 */
public class HourlyEmployee extends Employee {
    public HourlyEmployee(EmployeeRecord r) {
        super();
    }

    @Override
    public Boolean isPayDay() {
        return null;
    }

    @Override
    public Money calculatePay() {
        return null;
    }

    @Override
    public void deliverPay(Money e) {

    }
}
