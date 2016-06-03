import java.util.*;
import java.io.*;
public class BdayParadox
{
	public static void main(String[] args)
	{
		int num = 23;		//total number of samples taken each time for checking birthday paradox
		double total_groups = 10000;		//total number of groups for which birthday paradox is to be checked/validated
		int matches = 0;			//number of times birthdays match within a set
		int total =0;				//total times (ie. number of groups for which) birthday paradox holds true
		SampleDate[] people = new SampleDate[num];
		for(int n=0;n<total_groups;n++)
		{
			for(int i=0;i<num;i++)
			{
				people[i] = new SampleDate();
			}
			matches = 0;
			for(int i=0;i<num;i++)
			{
				for(int j=0;j<i;j++)
				{
					if((people[i].month == people[j].month) && (people[i].date==people[j].date))
						matches++;
				}
			}
			if(matches > 0)
				total+=1;
		}
		System.out.print("Birthday paradox holds true for ");
		System.out.printf("%.2f",(total/total_groups)*100);
		System.out.println("% of the total groups\n");
	}
}


class SampleDate
{
	Random rand = new Random();
	int month,date;
	public SampleDate()
	{
		month = rand.nextInt(12);
		if(month==2)
		{	date = rand.nextInt(28);
		}
		else if((month==4) || (month==6) || (month==9) || (month==11))
		{	date = rand.nextInt(30);
		}
		else
		{	date = rand.nextInt(31);
		}
	}
}
