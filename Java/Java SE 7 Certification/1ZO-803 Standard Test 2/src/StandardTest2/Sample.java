/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package StandardTest2;

/**
 *
 * @author t2p
 */
public class Sample implements IInt {

    public static void main(String[] args) {
        Sample s = new Sample(); //1 
        int j = s.thevalue; //2 
        int k = IInt.thevalue; //3 
        int l = thevalue; //4
    }
}
