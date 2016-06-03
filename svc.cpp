#include<iostream>
#include<bits/stdc++.h>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
	char ch;
	int flag=0;
	int len;
	int del_count=0;
	int count=0,vrcount=0;
	std::string str;
	ofstream current;
	std::string file;
	for(int i=0;;i++) 
	{
		if(vrcount!=0)
		{
			string strs="test";
			std::string r;
			ofstream fp;
			r=strs+std::to_string(vrcount);
			file=r+".txt";
			fp.open(file);
			string line;
 			ifstream myfile ("current_ver.txt");
 			if (myfile.is_open())
  			{
    				while ( getline (myfile,line) )
				{
					fp<<line<<"\n";
				}
				myfile.close();
			}

			cout<<vrcount<<endl;
			cout<<"enter the string"<<endl;
			cin>>str;

			len=str.length();
			current.open ("current_ver.txt", std::ofstream::out | std::ofstream::app);
			if(count<20)
			{
				cout<<len<<endl;
				if(len > 10)
				{
					std::string str2=str.substr(0,10);
					cout<<str2;
					current<<str2;
					current<<"\n";
				}
				else
				{
					cout<<str;
					current<<str;
					current<<"\n";
				}
				count++;
			}
		}

		else								//on 1st iteration
		{
			cout<<"enter the string"<<endl;
			cin>>str;
			len=str.length();
			current.open("current_ver.txt");
			if(len > 10)
			{
				std::string str2=str.substr(0,10);
				cout<<str2;
				current<<str2;
				current<<"\n";
			}
			else
			{
				cout<<str;
				current<<str;
				current<<"\n";
			}
			count++;
		}
		current.close();
	b:	cout<<"Do u want to continue(add(A) or delete(D))";
		cin>>ch;
		if(ch=='A')
		{
			vrcount++;
			continue;
		}
		else								// Delete i.e loading last version in current_ver
		{
			flag=1;
			vrcount++;
			string strs="test";
			std::string r;
			ofstream fp;
			r=strs+std::to_string(vrcount);
			file=r+".txt";
			fp.open(file);
			string line;
 			ifstream myfile ("current_ver.txt");
 			if (myfile.is_open())
  			{
    				while ( getline (myfile,line) )
				{
					fp<<line<<"\n";
				}
				myfile.close();
			}

			int ver = vrcount-1;
			if(del_count!=0)
			{	ver--;
			}


			r=strs+std::to_string(ver);
			file=r+".txt";
	 		ifstream temp(file);
			current.open("current_ver.txt");
			if (temp.is_open())
			{
				while ( getline (temp,line) )
				{
					current<<line<<"\n";
				}
				temp.close();
			}
			current.close();
			del_count++;
			vrcount--;
		}
		cout<<"\n";
		if(flag==1)
		{	goto b;
		}
	}
return 0;
}
