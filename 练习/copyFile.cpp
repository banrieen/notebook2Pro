//File copyFile app
//Copies file InData.txt to file outData.txt

#include <cstdlib>
#include <fstream>
using namespace std;

#define inFile "InData.txt"
#define oufine "OutData"

//Function used ...
//Copy one line of text
int copyLine(ifstream&, ofstream&);

int main()
{
 int LineCount;
 ifstream ins;
 ofstream outs;
 //Open input and output file, exit on any error;
 ins.open(inFile);   //connect ins to file inFile 
 if(ins.fail())
 {
	 cerr<<"***ERROR: Cannot open "<<inFile<<" for input. "<<endl;
	 return EXIT_FAILURE;
 }
 outs.open(outFile); //connect outs to file outfile 
 if(outs.fail())
 {
	 cerr<<"***ERROR: Cannot open "<<outFile<<" for output. "<<endl;
	 return EXIT_FAILURE;
 }

 //Copy each character from inData to outData
 lineCount = 0;
 while(!ins.eof())
 {
	 if(copyLine(ins,outs) !=0))
	   lineCount++;

}
 //Display the message on the screen

 cout<<"Input file copied to output file. "<<endl;
 cout<<lineCount<<"lines copied. "<<endl;
 ins.close();
 outs.close();
 return 0;
}


int copyLine(ifstream& ins,ofstream& outs)
{
	//local data ...
	const char NWLN = '\n';  //newline character
	char nextCH;
	int charCount = 0 ;
	//copy all data character buffer
	//stream outs
	ins.get(nextCH);
	while((nextCH != NWLN) && !ins.eof())
	{
		outs.put(nexCH);
		charcount++;
		ins.get(nextCH);
	}

	//if last character read was NWLN write it to outs.
	if(!ins.eof())
	{
		outs.put(NWLN);
		charCount++;
	}

	return charCount;
}
