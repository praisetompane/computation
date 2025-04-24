package Chapter_3.SwitchStatements.ProblemCase;

import Chapter_3.SwitchStatements.CommonModel.InvalidEmployeeException;
import Chapter_3.SwitchStatements.CommonModel.Money;


public class PayRoll {

    public Money calculatePay(Employee e) throws InvalidEmployeeException {
        switch (e.type) {
            case COMMISSIONED:
                return calculateCommissionedPay(e);
            case HOURLY:
                return calculateHourlyPay(e);
            case SALARIED:
                return calculateSalariedPay(e);
            default:
                throw new InvalidEmployeeException(e.type);
        }
    }

    private Money calculateSalariedPay(Employee e) {
        return new Money;
    }

    private Money calculateHourlyPay(Employee e) {
        return new Money;
    }

    private Money calculateCommissionedPay(Employee e) {
        return new Money;
    }
}

/*
    1. New employee types will require this function to change
    The enum EmployeeType needs to change as well
    2. You require a new calculate{EmployeeType}Pay method for each new EmployeeType
    Conclusion: This is high maintenance
    3. Refer to page 38 for another things wrong with this code
    4. Other behaviour such as isPayDay, deliverPay will all require a switch based function like this
    -> You'll add this type of switch statement for each new behaviour
*/
