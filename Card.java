/*
 * Card.java
 *
 * A blueprint class for objects that represent a single playing card
 * that has a rank and a suit.
 * 
 * starter code: CS 112 Staff (cs112-staff@cs.bu.edu)
 * completed by: Maarten Lopes lopesmaa@bu.edu
 */

public class Card {
    /* constants for the ranks of non-numeric cards */
    public static final int ACE = 1;
    public static final int JACK = 11;
    public static final int QUEEN = 12;
    public static final int KING = 13;
    
    /* other constants for the ranks */
    public static final int FIRST_RANK = 1;
    public static final int LAST_RANK = 13;
    
    /* 
     * class-constant array containing the string representations
     * of all of the card ranks. 
     * The string for the numeric rank r is given by RANK_STRINGS[r].
     */
    public static final String[] RANK_STRINGS = {
      null, "A", "2", "3", "4", "5", "6",
      "7", "8", "9", "10", "J", "Q", "K"
    };
    
    /* 
     * class-constant array containing the char representations
     * of all of the possible suits.
     */
    public static final char[] SUITS = {'C', 'D', 'H', 'S'};

    
    /* Put the rest of the class definition below. */

    /*method that goes in the reverse direction – taking a rank string as its only parameter and returning the corresponding integer rank. 
    In other words, the method should find and return the index of the specified rank string in the RANK_STRINGS array */
    public static int rankNumFor(String typ) {
      if (typ == null) {
        return -1;
      }
      for (int i = 1; i < RANK_STRINGS.length; i++) {
        if (typ == RANK_STRINGS[i]) {
          return i;
        }
      }
      return -1;
    }

    /* takes a single-character representation of a card’s suit and returns true if that suit is valid 
    (i.e., if it is one of the values in the SUITS array), and false otherwise */
    public static boolean isValidSuit(char suit) {
      for (int i = 0; i < SUITS.length; i++) {
        if (suit == SUITS[i]) {
          return true;
        }
      }
      return false;
    }

    private int rank;
    private char suit;

    public Card (int rank, char suit) {
      /*constructor that takes two parameters: an integer specifying the card’s rank, and a single character (a char) specifying 
      the card’s suit (in that order) */
      if (isValidSuit(suit) == false) {
        throw new IllegalArgumentException();
      }
      else if (rank < 1 || rank > 13) {
        throw new IllegalArgumentException();
      }
      else{
        this.rank = rank;
        this.suit = suit;
      }
    }

    public Card (String rank) {
      /*constructor that takes a single parameter: a two- or three-character string that specifies the card to be created */
      if (rank == null) {
        throw new IllegalArgumentException();
      }
      String vrank = rank.substring(0, rank.length() - 1);
      char srank = rank.charAt(rank.length() - 1);
      if (isValidSuit(srank) == false) {
        throw new IllegalArgumentException();
      }
      else if (vrank.length() == 2 && vrank.charAt(1) > '0') {
        throw new IllegalArgumentException();
      }
      else {
        for (int i = 0; i < RANK_STRINGS.length; i++) {
          if (vrank.equals(RANK_STRINGS[i])) {
            this.rank = i;
          }
        }
        this.suit = srank;
      }
    }

    /*returns the integer representing the Card object’s rank */
    public int getRank() {
      return this.rank;
    }
    /*returns the char representing the Card object’s suit */
    public char getSuit() {
      return this.suit;
    }
    /*returns true if the Card is an Ace and false if it is not */
    public boolean isAce() {
      if (this.getRank() == 1) {
        return true;
      }
      return false;
    }
    /*returns true if the Card is a face card (Jack, Queen, or King) and and false if it is not */
    public boolean isFaceCard() {
      if (this.getRank() == 11 || this.getRank() == 12 || this.getRank() == 13) {
        return true;
      }
      return false;
    }
    /*returns the Card object’s value */
    public int getValue() {
      if (this.isFaceCard() == true) {
        return 10;
      }
      else if (this.isAce() == true) {
        return 1;
      }
      else {
        return this.getRank();
      }
    }
    /*method that returns a String representation of the Card object that can be used when printing it or concatenating it to a String */
    public String toString() {
      return RANK_STRINGS[this.rank] + "" + this.suit;
    }

    /*takes a Card object as a parameter and determines if it is has the same suit as the called object, returning true if they 
    have the same suit and false if they do not have the same suit */
    public boolean sameSuitAs(Card other) {
      return (other != null && this.suit == other.suit);
      }
    
    /*takes a Card object as a parameter and determines if it is equivalent to the called object, returning true if it is 
    equivalent and false if it is not equivalent */
    public boolean equals(Card other) {
      return (other != null && this.suit == other.suit && this.rank == other.rank);
    }

    
    public static void main(String[] args) {
    System.out.println(rankNumFor("10"));
    System.out.println(isValidSuit('B')); 
  }

}
