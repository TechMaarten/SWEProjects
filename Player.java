import java.util.*;

public class Player {
    private String name;
    private Card[] hand;
    private int numCards;

    public Player(String name) {
        /*a constructor that takes a single parameter for the name of the player. It should initialize all of the fields */
        this.name = name;
        this.numCards = 0;
        this.hand = new Card[Blackjack.MAX_CARDS_PER_PLAYER];
    }
    public String getName() {
        /*an accessor named getName that returns the player’s name. */
        return this.name;
    }
    public int getNumCards() {
        /*an accessor named getNumCards that returns the current number of cards in the player’s hand. */
        return this.numCards;
    }
    public String toString(){
        /*a toString method that just returns the player’s name. */
        return getName();
    }
    public void addCard(Card i) {
        /*a mutator named addCard that takes a Card object as a parameter and adds the specified 
        card to the player’s hand, filling the array from left to right */
        if (i == null) {
            throw new IllegalArgumentException();
        }
        else if (this.numCards == this.hand.length) {
            throw new IllegalArgumentException();
        }
        else {
            this.hand[this.numCards] = i;
            numCards++;
        }
    }
    public Card getCard(int index) {
        /*an accessor named getCard that takes an integer index as a parameter and returns the Card at the specified 
        position in the player’s hand */
        if (index >= this.hand.length || this.hand[index] == null) {
            throw new IllegalArgumentException();
        }
        return this.hand[index];
    }
    public int getHandValue() {
        /*an accessor method named getHandValue that computes and returns the total value of the player’s current hand  */
        int handval = 0;
        for (int i = 0; i < getNumCards(); i++) {
            if (this.hand[i].getValue() == Card.ACE && handval + 11 <= 21) {
                handval += 11;
            } 
            else if (this.hand[i].getValue() == Card.ACE && handval + 11 > 21) {
                handval += 1;
            }
            else {
                handval += this.hand[i].getValue();
            }
        }
        return handval;
    }
    public void printHand() {
        /*an accessor method named printHand that prints the current contents of the player’s hand, followed by the value 
        of the player’s hand */
        String x = "";
        for (int i = 0; i < getNumCards(); i++) {
            x += this.hand[i] + "  ";
        }
        System.out.println(x + "(value = " + getHandValue() + ")");
    }
    public boolean hasBlackjack() {
        /*an accessor method named hasBlackjack that returns true if the player has Blackjack (a two-card hand with a value of 21),
         and false otherwise */
        if (getNumCards() == 2 && getHandValue() == 21) {
            return true;
        }
        return false;
    }
    public boolean wantsHit(Scanner scan, Player opp) {
        /*an accessor method called wantsHit that should return true if the player wants another hit, and false if 
        the player does not want another hit. */
        System.out.print("Want another hit, " + getName() + " (y/n)? ");
        String choice = scan.nextLine();
        String y = "y";
        String Y = "Y";
        if (choice.equals(y) || choice.equals(Y)) {
            return true;
        }
        else {
            return false;
        }
    }
    public void discardCards() {
        /*a mutator method called discardCards that should get rid of all of the cards in the player’s hand, to prepare for a 
        new round of the game.  */
        for (int i = 0; i < getNumCards(); i++) {
            if (this.hand[i] != null) {
                this.hand[i] = null;
            }
        }
        this.numCards = 0;
    }

}