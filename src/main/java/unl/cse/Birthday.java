package unl.cse;

import org.joda.time.DateTime;
import org.joda.time.Interval;
import org.joda.time.Period;

/**
 * Computes the number of days until the user's next birthday.
 * @author eric
 *
 */
public class Birthday {
	public static void main(String args[]) {

		String name = "Eric";

		int month = 1;
		int date = 3;
		int year = 2002;

		DateTime bday = new DateTime(year, month, date, 0, 0);
		DateTime today = new DateTime();

		Period age = new Period(bday, today);

		int years = age.getYears();
		int months = age.getMonths();
		int days = age.getWeeks() * 7 + age.getDays();

		DateTime nextBday = new DateTime(year + years + 1, month, date, 0, 0);
		Interval daysToNextBdayI = new Interval(today, nextBday);
		double daysRemaining = daysToNextBdayI.toDurationMillis() / (1000 * 60 * 60 * 24) + 1;

		// TODO: write code to output results here
		System.out.printf("Hello %s. Today you are %d years, %d months, and %d days old.\n", name, years, months, days);
		if (months == 0 && days == 0) {
			System.out.println("Happy Birthday!");
		} else {
			System.out.printf("Your friends have %f shopping days until your next birthday.\n", daysRemaining);
		}
	}
}
