import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.Scanner;
 
public class BirthdayParadox
{
 
	private static final Random randGen = new Random();
 
	static float simulate(int nPeople, int nTrials)
	{
        	int count = 0;
        	for(int i = 0; i < nTrials; i++)
		{
			if(trial(nPeople))
				count++;
        	}
		return (float) count/nTrials;
	}
 
	static boolean trial(int nPeople)
	{
        	Set<Integer> birthdays = new HashSet<Integer>();
	        for (int i = 0; i < nPeople; i++)
		{
	            	int day = randGen.nextInt(365);
	            	if (birthdays.contains(day))
				return true;
			birthdays.add(day);
	        }
	        return false;
	}
 
	public static void main(String[] args)
	{
		System.out.println("Enter number of People:\t");
		Scanner scan = new Scanner(System.in);
		int np = scan.nextInt();
		System.out.println("Enter number of Trials:\t");
		int nt = scan.nextInt();
        	System.out.printf("%.4f\n", simulate(np, nt));
	}
}
