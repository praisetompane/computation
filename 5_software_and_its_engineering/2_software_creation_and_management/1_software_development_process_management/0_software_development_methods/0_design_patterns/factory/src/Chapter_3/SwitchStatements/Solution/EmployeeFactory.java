package Chapter_3.SwitchStatements.Solution;

import Chapter_3.SwitchStatements.CommonModel.InvalidEmployeeException;
import Chapter_3.SwitchStatements.Solution.Model.*;

/**
 * Created by Praise on 2016/08/21.
 */
public interface EmployeeFactory {
    public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeException;
}

