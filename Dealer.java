import java.util.*;

public class Dealer extends Player {
    private boolean reveal;

    public Dealer() {
        /*its own constructor, which takes no parameters. It should call the constructor of the superclass to do the work of initializing 
        the inherited fields, passing it the string “dealer” as the name of the player */
        super("dealer");
        this.reveal = false;
    }
    public void revealFirstCard() {
        /*a mutator method called revealFirstCard that takes no parameters and changes the value of the called object’s boolean field to 
        indicate that the dealer’s first card should now be revealed. */
        this.reveal = true;
    }
    public void printHand() {
        /*a printHand method that overrides the inherited version of that method.  */
        if (this.reveal == true) {
            super.printHand();
        }
        else {
            if (super.getNumCards() <= 2) {
                System.out.println("XX" + "  " + super.getCard(1));
            }
            else {
                System.out.println("XX" + "  " + super.getCard(1) + "  " + super.getCard(2));
            }
        }
    }
    public boolean wantsHit(Scanner scan, Player opp) {
        /*a wantsHit method that overrides the inherited version of that method. This version of the method 
        should determine if the dealer should give herself another hit */
        if (opp.getHandValue() < 17 && super.getHandValue() < 17) {
            return true;
        }
        else if (opp.getHandValue() < 17 && super.getHandValue() >= 17) {
            return false;
        }
        else if (opp.getHandValue() >= 17 && super.getHandValue() < 17) {
            return true;
        }
        else if (opp.getHandValue() > 21) {
            return false;
        }
        return false;
    }
    public void discardCards() {
        /*a discardCards method that overrides the inherited version of that method. This version of the method should have 
        the same effect as the inherited version of the method.  */
        this.reveal = false;
        super.discardCards();
    }


}




