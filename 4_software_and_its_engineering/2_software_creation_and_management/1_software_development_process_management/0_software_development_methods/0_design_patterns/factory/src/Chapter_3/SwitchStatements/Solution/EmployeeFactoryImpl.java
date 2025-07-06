package Chapter_3.SwitchStatements.Solution;

import Chapter_3.SwitchStatements.CommonModel.InvalidEmployeeException;
import Chapter_3.SwitchStatements.Solution.Model.*;

/**
 * Created by Praise on 2016/08/21.
 */

public class EmployeeFactoryImpl implements EmployeeFactory{
    @Override
    public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeException {
        switch (r.type) {
            case COMMISSIONED:
                return new CommissionedEmployee(r);
            case HOURLY:
                return new HourlyEmployee(r);
            case SALARIED:
                return new SalariedEmployee(r);
            /*You would still add a new Entry for any new Employee type
            That class would implement all the behaviour of an Employee
                -> You WOULDN'T though have to REMEMBER to update the n other Switch statements for mwthods such
                as isPayDay, deliverPay etc {definitely easier maintenance}*/
            default:
                throw new InvalidEmployeeException(r.type);
        }
    }
}