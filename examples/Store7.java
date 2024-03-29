// -----------
// Store7.java
// -----------

/*
Remove Price.getPriceCode()
Remove Move.getPriceCode()
Change Price to an interface
Create AbstractPrice
Create Movie.getOutput()
Create Rental.getOutput()
Remove Customer.getTotalCharge()
Remove Customer.getTotalFrequentRenterPoints()
Use Class.forName()
Rename getCharge()             to getAmount().
Rename getFrequentRenterPoints to getPoints()
*/

import java.util.Vector;

interface Price {
    double getAmount (int daysRented);
    int    getPoints (int daysRented);}

abstract class AbstractPrice implements Price {
    public int getPoints (int daysRented) { // const
        return 1;}}

class RegularPrice extends AbstractPrice {
    public final double getAmount (int daysRented) { // const
        double result = 2;
        if (daysRented > 2)
            result += (daysRented - 2) * 1.5;
        return result;}}

class NewReleasePrice extends AbstractPrice {
    public final double getAmount (int daysRented) { // const
        return daysRented * 3;}

    public final int getPoints (int daysRented) { // const
        return (daysRented > 1) ? 2 : 1;}}

class ChildrensPrice extends AbstractPrice {
    public final double getAmount (int daysRented) { // const
        double result = 1.5;
        if (daysRented > 3)
            result += (daysRented - 3) * 1.5;
        return result;}}

class Movie {
    public static final String REGULAR     = "RegularPrice";
    public static final String NEW_RELEASE = "NewReleasePrice";
    public static final String CHILDRENS   = "ChildrensPrice";

    private String _title;
    private Price  _price;

    public Movie (String title, String price) {
        _title = title;
        try {
            _price = (Price) Class.forName(price).newInstance();}
        catch (ClassCastException e) {
            e.printStackTrace();}
        catch (ClassNotFoundException e) {
            e.printStackTrace();}
        catch (IllegalAccessException e) {
            e.printStackTrace();}
        catch (InstantiationException e) {
            e.printStackTrace();}}

    /**
     * _price
     *     getAmount()
     */
    public double getAmount (int daysRented) { // const
        return _price.getAmount(daysRented);}

    /**
     * _price
     *     getPoints()
     */
    public int getPoints (int daysRented) { // const
        return _price.getPoints(daysRented);}

    public String getOutput (int daysRented) { // const
        return
            "\t" + _title                                +
            "\t" + String.valueOf(getAmount(daysRented)) + "\n";}

    public String getTitle () { // const
        return _title;}

    public void setPrice (Price price) {
        _price = price;}}

class Rental {
    private Movie _movie;
    private int   _daysRented;

    public Rental (Movie movie, int daysRented) {
        _movie      = movie;
        _daysRented = daysRented;}

    /**
     * _movie
     *     getAmount()
     */
    public double getAmount () { // const
        return _movie.getAmount(_daysRented);}

    public int getDaysRented () { // const // no longer used
        return _daysRented;}

    public Movie getMovie () { // const
        return _movie;}

    /**
     * _movie
     *     getPoints()
     */
    public int getPoints () { // const
        return _movie.getPoints(_daysRented);}

    /**
     * _movie
     *     getOutput()
     */
    public String getOutput () { // const
        return _movie.getOutput(_daysRented);}}

class Customer {
    private String         _name;
    private Vector<Rental> _rentals = new Vector<Rental>();

    public Customer (String name) {
        _name = name;}

    public void addRental (Rental rental) {
        _rentals.addElement(rental);}

    public String getName () { // const
        return _name;}

    /**
     * _rentals
     *     getAmount()
     *     getPoints()
     *     getOutput()
     */
    public String statement () { // O(3n)
        double amount = 0;
        for (Rental rental : _rentals)
            amount += rental.getAmount();
        int points = 0;
        for (Rental rental : _rentals)
            points += rental.getPoints();
        String result = "Rental Record for " + getName() + "\n";
        for (Rental rental : _rentals)
            result += rental.getOutput();
        result += "Amount owed is " + String.valueOf(amount) + "\n";
        result += "You earned " + String.valueOf(points) + " frequent renter points";
        return result;}}

final class Store7 {
    public static void main (String[] args) {
        System.out.println("Store7.java");

        Customer x = new Customer("Penelope");
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "Amount owed is 0.0\n"         +
            "You earned 0 frequent renter points");

        x.addRental(new Rental(new Movie("Shane", Movie.REGULAR), 2));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "Amount owed is 2.0\n"         +
            "You earned 1 frequent renter points");

        x.addRental(new Rental(new Movie("Red River", Movie.REGULAR), 5));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "Amount owed is 8.5\n"         +
            "You earned 2 frequent renter points");

        x.addRental(new Rental(new Movie("Giant", Movie.NEW_RELEASE), 1));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "Amount owed is 11.5\n"        +
            "You earned 3 frequent renter points");

        x.addRental(new Rental(new Movie("2001", Movie.NEW_RELEASE), 3));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "Amount owed is 20.5\n"        +
            "You earned 5 frequent renter points");

        x.addRental(new Rental(new Movie("Big Country", Movie.CHILDRENS), 3));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "Amount owed is 22.0\n"        +
            "You earned 6 frequent renter points");

        x.addRental(new Rental(new Movie("Spartacus", Movie.CHILDRENS), 5));
        assert x.statement().equals(
            "Rental Record for Penelope\n" +
            "\tShane\t2.0\n"               +
            "\tRed River\t6.5\n"           +
            "\tGiant\t3.0\n"               +
            "\t2001\t9.0\n"                +
            "\tBig Country\t1.5\n"         +
            "\tSpartacus\t4.5\n"           +
            "Amount owed is 26.5\n"        +
            "You earned 7 frequent renter points");

        System.out.println("Done.");}}
