#!/bin/sh
#
# xpl2gpl is a utility that converters tcptrace-style xplot input to gnuplot input.
#
# Avinash Lakhiani <avinash.lakhiani@ohiou.edu>, Ohio Universtiy.
#
# July 15, 2001

# Argument checking
if [ $# -eq 1 ]
then

# Extracting file-basename from the xplot filename 
BASENAME=`basename $1 .xpl`
rm -f ${BASENAME}.dataset.*.* ${BASENAME}.gpl ${BASENAME}.ps ${BASENAME}.files ${BASENAME}.datasets ${BASENAME}.labels

# AWK starts here
gawk -v BASENAME=$BASENAME '

# This function returns the filename in which data is to be stored based on color
# and style.
# It also stores the syle of the plot in an array for classification when all
# datasets are merged at the end of the script.
function data_set_name(color, style)   
 {
    entered = 1;
    array_index = color "." style; 
    ++dataset_type[array_index];
    file_style[array_index] = style;
    return(BASENAME ".dataset." color "." style);
}

# This function returns the dataset filename. Used when the ".gpl" file is being
# created.
function file_name(dataset)
{
    return(BASENAME ".dataset." dataset);
}

# This function sets the x & y -axis formats
function format_to(datatype) {
	if (datatype == "unsigned")
		return("%.0f");
	if (datatype == "signed")
		return("%.0f");
	if (datatype == "double")
		return("%.0f");
	if (datatype == "timeval")
		return("%.0f");
	if (datatype == "dtime")
		return("%.0f");
	printf("Unknown datatype: \"%s\"\n", datatype) > "/dev/tty";
	exit;
}

# Initializations
BEGIN	   {
		TITLE=FILENAME;
		XLABEL="x";
		YLABEL="y";

		# Indicates the current color and style for the plot
		current_dataset_color = "null";
		current_dataset_style = "null";
		
		# Stores previous state information
		prev_dataset_color = "null";
		prev_dataset_style = "null";
		
		# All files used during conversion
		remove_files = BASENAME ".dataset.*.*";     # Stores the list of files to be deleted after conversion is complete
		gpl_file = BASENAME ".gpl";		    # The final generated gnuplot file
		labels_file = BASENAME ".labels"            # Stores all the labels in the plot
		printf("") >> labels_file;
		current_dataset_file = "/nofile";           # Stores the filename for the current dataset
		dataset_final_file = BASENAME ".datasets";  # The final file containing all the data that is to be plotted		
		dataset_file = BASENAME ".files";	    # Contains the list of dataset files that are to be concatenated to generated the final dataset file	
		printf("#!/bin/sh\ncat ") >> dataset_file;  # These two lines create the script file for final concatenation
		system("chmod u+x " dataset_file);		
		
		# Inital Values
		initial_x=-1.;               
		initial_y=-1.;
		dataset_index=-1.;
		entered = 0;
		min_xpoint = 9999999999.0;
		max_xpoint = 0.0;
		min_ypoint = 9999999999.0;
		max_ypoint = 0.0;
		label_index = 0;
		
		#No. of sec. from Jan 01, 1970 to Jan 01, 2000
		secs_2000=946684800.0;
		
		# get the axis types
		getline;
		xaxis_type=$1;
		yaxis_type=$2;
		xaxis_format=format_to(xaxis_type);
		yaxis_format=format_to(yaxis_type);
	   }

# Parsing begins here
# Valid plotting styles in xplot:-
# title, xlabel, ylabel, COLOR(as below), ltext, dot, line , diamond, box, uarrow,
# darrow, larrow, rarrow, utick, dtick, ltick, rtick, vtick, htick, dline, atext,
# go.

# What the action statements below do:-
# For all the patterns, the corresponding actions behave more or less the same.
# Depending on the current color and style, the function data_set_name returns the
# corresponding filename. The x & y co-ordinates are then written to this file.

/^title$/  { getline; TITLE=$0; next; }
/^xlabel$/ { getline; XLABEL=$0; next; }
/^ylabel$/ { getline; YLABEL=$0; next; }


/^((white)|(green)|(red)|(blue)|(yellow)|(purple)|(orange)|(magenta)|(pink))$/ {
		 current_dataset_color = $1;
		 next;
		}


/^dot .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	
			

/^line .*$/	{
			current_dataset_style = $1;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x1point=$4;
			y1point=$5;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			printf("\n") >> current_dataset_file;
			next;
		}


/^diamond .*$/	{
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^box .*$/	{
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^((uarrow)|(darrow))/   {
			if(NR == 4)
			    prev_dataset_color = $4;
			else
			    prev_dataset_color = current_dataset_color;
			
			prev_dataset_style = $1;	
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			getline;
			if(NR == 4)
			    current_dataset_color = $4;
	
			x1point=$2;
			y1point=$3;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;

			if(NR == 5)
			{
			    x2point=$4;
			    y2point=$5;
			    if(min_xpoint > x2point)
			      min_xpoint = x2point;
			    if(max_xpoint < x2point)
			      max_xpoint = x2point;
			    if(min_ypoint > y2point)
			      min_ypoint = y2point;
			    if(max_ypoint < y2point)
			      max_ypoint = y2point;
			}
			current_dataset_style = $1;

			if(((prev_dataset_style == "uarrow" && current_dataset_style == "darrow") || (prev_dataset_style == "darrow" && current_dataset_style == "uarrow")) && (xpoint == x1point && ypoint == y1point) && (current_dataset_color == prev_dataset_color))			
			{
			    current_dataset_style = "cross";
			    current_dataset_file = data_set_name(current_dataset_color, current_dataset_style);
			    printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			    next;
			 }

			 else
			 {
			    current_dataset_file = data_set_name(prev_dataset_color, prev_dataset_style);
			    printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			    current_dataset_file = data_set_name(current_dataset_color, current_dataset_style);
			    printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			    if(current_dataset_style == "line" || current_dataset_style == "dline")
			    {
				printf("%f %f\n", x1point, y1point) >> current_dataset_file;
				printf("\n") >> current_dataset_file;
			    }
				
			    next;
			} 
		  }
			    
/^dtick .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	

/^utick .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	

/^x .*$/        {
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}		

/^plus .*$/     {
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^(ltick)|(rtick)|(htick)|(vtick) .*$/  {
 			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}


/^(larrow)|(rarrow) .*$/  {
    			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^dline .*$/    {
			current_dataset_style = $1;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x1point=$4;
			y1point=$5;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			printf("\n") >> current_dataset_file;
			next;
		}



/^atext .*$/    {
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x_pt[label_index] = xpoint;
			y_pt[label_index] = ypoint;
			label_dir[label_index] = +1;
                        getline;
                        label[label_index++] = $0;
			next;
		}

/^btext .*$/    {
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x_pt[label_index] = xpoint;
			y_pt[label_index] = ypoint;
			label_dir[label_index] = -1;
                        getline;
                        label[label_index++] = $0;
			next;
		}


/^ltext.*$/	{
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        if(NR == 4)
			  current_dataset_color = $4;
			getline;
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f right\n", $0, xpoint, secs_2000, ypoint) >> labels_file;
			else printf("set label \"%s\" at %f, %f right\n", $0, xpoint, ypoint) >> labels_file;
			next;
		}

/^rtext.*$/	{
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        if(NR == 4)
			  current_dataset_color = $4;
			getline;
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f left\n", $0, xpoint, secs_2000, ypoint) >> labels_file;
			else printf("set label \"%s\" at %f, %f left\n", $0, xpoint, ypoint) >> labels_file;
			next;
		}


/^go$/		{next}


                { printf("Bad line %d: \"%s\"\n", NR, $0); next; }


# Creating the gnuplot file and deleting all the dataset files after concatenating all contents into one file

END	{

		printf("set title \"%s\"\n", TITLE) >> gpl_file;
		printf("set xlabel \"%s\"\n", XLABEL) >> gpl_file;
		printf("set ylabel \"%s\"\n", YLABEL) >> gpl_file;
		printf("set format x \"%s\"\n", xaxis_format) >> gpl_file;
		printf("set format y \"%s\"\n", yaxis_format) >> gpl_file;
		if(xaxis_type == "timeval" || xaxis_type == "dtime") {
		  printf("set xdata time\n") >> gpl_file;
		}
		printf("set nokey\n") >> gpl_file;
		printf("load \"%s\";\n", labels_file) >> gpl_file;
		
		first = 1;

		if(entered)
		{
 		for (dataset in dataset_type)
		{
		    
		    FILE=file_name(dataset);
		    if (first)
			printf("plot ") >> gpl_file;
		    else
			printf(", ") >> gpl_file;
		    first = 0;
		    printf("\"%s\" ", dataset_final_file) >> gpl_file;

 		    if(file_style[dataset] == "dot")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with dots", ++dataset_index) >> gpl_file;
			else printf("index %d with dots", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "line")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with lines", ++dataset_index) >> gpl_file;
			else printf("index %d with lines", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;    
		    }	
		    if(file_style[dataset] == "diamond") 
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 1", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 1", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "box")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 3", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 3", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "cross") 
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 4", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 4", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "uarrow") 
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 1", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 1", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "darrow") 
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 1", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 1", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "dtick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "utick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "x")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 4", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 4", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "plus")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "ltick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "rtick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "htick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "vtick")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 2", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 2", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }

		    if(file_style[dataset] == "larrow")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 5", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 5", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "rarrow")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with points pt 5", ++dataset_index) >> gpl_file;
			else printf("index %d with points pt 5", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		    if(file_style[dataset] == "dline")
		    {
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("index %d using ($1-946684800.0):2 with linespoints pt 4", ++dataset_index) >> gpl_file;
			else printf("index %d with linespoints pt 4", ++dataset_index) >> gpl_file;
			printf("\n\n") >> FILE;
			close( FILE );
			printf("%s ", FILE) >> dataset_file;
		    }
		}
		for(l=0; l < label_index; l++)
		{
		  xpoint = x_pt[l];
		  ypoint = y_pt[l];
		  if(max_ypoint > 0 && label_dir[l] == -1) ypoint = ypoint - (50000000 * ((max_ypoint - min_ypoint)/max_ypoint));		  
		  if(max_ypoint > 0 && label_dir[l] == +1) ypoint = ypoint + (50000000 * ((max_ypoint - min_ypoint)/max_ypoint));
		  curr_label = label[l];
		  if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f center\n", curr_label, xpoint, secs_2000, ypoint) >> labels_file;
		  else printf("set label \"%s\" at %f, %f center\n", $1, xpoint, ypoint) >> labels_file;

		}
		}
		printf(";\n") >> gpl_file;
		printf("set term postscript\n") >> gpl_file;
		printf("set output \"%s.ps\"\n", BASENAME) >> gpl_file;
		printf("replot\n") >> gpl_file;
		printf("pause -1;\n") >> gpl_file;
		close( gpl_file );
		close( labels_file );
		printf("> %s", dataset_final_file) >> dataset_file;
		close( dataset_file );

# Concatenting all the datasets and deleting the individual files

		if(entered)
		  system("./" dataset_file);
		system("rm -f " remove_files);
		system("rm -f " dataset_file);
	}	
' $1 # end of AWK

elif [ "$1" = "-s" ]  #'-s' option part
then

# Extracting file-basename from the xplot filename 
BASENAME=`basename $2 .xpl`
rm -f ${BASENAME}.dataset.*.* ${BASENAME}.gpl ${BASENAME}.ps ${BASENAME}.files ${BASENAME}.datasets ${BASENAME}.labels

gawk -v BASENAME=$BASENAME '

# This function returns the filename in which data is to be stored based on color and style
# It also stores the syle of the plot in an array for classification when all datasets are merged at the end of the script

function data_set_name(color, style)
 {
    entered = 1;
    array_index = color "." style; 
    ++dataset_type[array_index];
    file_style[array_index] = style;
    return(BASENAME ".dataset." color "." style);
}

# This function returns the dataset filename
# Used when the ".gpl" file is being created

function file_name(dataset)
{
    return(BASENAME ".dataset." dataset);
}

# This function sets the x & y -axis formats

function format_to(datatype) {
	if (datatype == "unsigned")
		return("%.0f");
	if (datatype == "signed")
		return("%.0f");
	if (datatype == "double")
		return("%.0f");
	if (datatype == "timeval")
		return("%.0f");
	if (datatype == "dtime")
		return("%.0f");
	printf("Unknown datatype: \"%s\"\n", datatype) > "/dev/tty";
	exit;
}
# This function sets the x & y -axis formats


BEGIN	   {
		TITLE=FILENAME;
		XLABEL="x";
		YLABEL="y";
		
		# Indicates the current color and style for the plot
		current_dataset_color = "null";
		current_dataset_style = "null";

		# Stores previous state information
		prev_dataset_color = "null";
		prev_dataset_style = "null";


		remove_files = BASENAME ".dataset.*.*";     # Stores the list of files to be deleted after conversion is complete
		gpl_file = BASENAME ".gpl";		    # The final generated gnuplot file
		labels_file = BASENAME ".labels"            # Stores all the labels in the plot
		printf("") >> labels_file;
		current_dataset_file = "/nofile";           # Stores the filename for the current dataset 

		# Inital Values
		labels_present = 0;
		initial_x=-1.;
		initial_y=-1.;
		dataset_index=-1.;
		entered = 0;
		min_xpoint = 9999999999.0;
		max_xpoint = 0.0;
		min_ypoint = 9999999999.0;
		max_ypoint = 0.0;
		label_index = 0;
		
		#No. of sec. from Jan 01, 1970 to Jan 01, 2000
		secs_2000=946684800.0;
		
		# get the axis types
		getline;
		xaxis_type=$1;
		yaxis_type=$2;
		xaxis_format=format_to(xaxis_type);
		yaxis_format=format_to(yaxis_type);
	   }

# Parsing begins here
# Valid plotting styles in xplot:-
# title, xlabel, ylabel, COLOR(as below), ltext, dot, line , diamond, box, uarrow,
# darrow, larrow, rarrow, utick, dtick, ltick, rtick, vtick, htick, dline, atext,
# go.

# What the action statements below do:-
# For all the patterns, the corresponding actions behave more or less the same.
# Depending on the current color and style, the function data_set_name returns the
# corresponding filename. The x & y co-ordinates are then written to this file.


/^title$/  { getline; TITLE=$0; next; }
/^xlabel$/ { getline; XLABEL=$0; next; }
/^ylabel$/ { getline; YLABEL=$0; next; }


/^((white)|(green)|(red)|(blue)|(yellow)|(purple)|(orange)|(magenta)|(pink))$/ {
		 current_dataset_color = $1;
		 next;
		}



/^dot .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	
			

/^line .*$/	{
			current_dataset_style = $1;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x1point=$4;
			y1point=$5;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			printf("\n") >> current_dataset_file;
			next;
		}


/^diamond .*$/	{
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^box .*$/	{
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^((uarrow)|(darrow))/   {
			if(NR == 4)
			    prev_dataset_color = $4;
			else
			    prev_dataset_color = current_dataset_color;
			
			prev_dataset_style = $1;	
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			getline;
			if(NR == 4)
			    current_dataset_color = $4;
	
			x1point=$2;
			y1point=$3;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;

			if(NR == 5)
			{
			    x2point=$4;
			    y2point=$5;
			    if(min_xpoint > x2point)
			      min_xpoint = x2point;
			    if(max_xpoint < x2point)
			      max_xpoint = x2point;
			    if(min_ypoint > y2point)
			      min_ypoint = y2point;
			    if(max_ypoint < y2point)
			      max_ypoint = y2point;
			}
			current_dataset_style = $1;

			if(((prev_dataset_style == "uarrow" && current_dataset_style == "darrow") || (prev_dataset_style == "darrow" && current_dataset_style == "uarrow")) && (xpoint == x1point && ypoint == y1point) && (current_dataset_color == prev_dataset_color))			
			{
			    current_dataset_style = "cross";
			    current_dataset_file = data_set_name(current_dataset_color, current_dataset_style);
			    printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			    next;
			 }

			 else
			 {
			    current_dataset_file = data_set_name(prev_dataset_color, prev_dataset_style);
			    printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			    current_dataset_file = data_set_name(current_dataset_color, current_dataset_style);
			    printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			    if(current_dataset_style == "line" || current_dataset_style == "dline")
			    {
				printf("%f %f\n", x1point, y1point) >> current_dataset_file;
				printf("\n") >> current_dataset_file;
			    }
				
			    next;
			} 
		  }
			    
/^dtick .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	

/^utick .*$/      {
			current_dataset_style = $1;
			if(NF == 4)
			    current_dataset_color = $4;
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}	

/^x .*$/        {
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}		

/^plus .*$/     {
			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^(ltick)|(rtick)|(htick)|(vtick) .*$/  {
 			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}


/^(larrow)|(rarrow) .*$/  {
    			current_dataset_style = $1;
			if(NR == 4)
			    current_dataset_color = $4;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			next;
		}

/^dline .*$/    {
			current_dataset_style = $1;
			current_dataset_file = data_set_name(current_dataset_color, current_dataset_style); 
			xpoint=$2;
			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x1point=$4;
			y1point=$5;
			if(min_xpoint > x1point)
			  min_xpoint = x1point;
			if(max_xpoint < x1point)
			  max_xpoint = x1point;
			if(min_ypoint > y1point)
			  min_ypoint = y1point;
			if(max_ypoint < y1point)
			  max_ypoint = y1point;
			printf("%f %f\n", xpoint, ypoint) >> current_dataset_file;
			printf("%f %f\n", x1point, y1point) >> current_dataset_file;
			printf("\n") >> current_dataset_file;
			next;
		}

/^atext .*$/    {
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x_pt[label_index] = xpoint;
			y_pt[label_index] = ypoint;
			label_dir[label_index] = +1;
                        getline;
                        label[label_index++] = $0;
			next;
		}

/^btext .*$/    {
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
			x_pt[label_index] = xpoint;
			y_pt[label_index] = ypoint;
			label_dir[label_index] = -1;
                        getline;
                        label[label_index++] = $0;
			next;
		}


/^ltext.*$/	{
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        if(NR == 4)
			  current_dataset_color = $4;
			getline;
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f right\n", $0, xpoint, secs_2000, ypoint) >> labels_file;
			else printf("set label \"%s\" at %f, %f right\n", $0, xpoint, ypoint) >> labels_file;
			next;
		}

/^rtext.*$/	{
			xpoint=$2;
  			ypoint=$3;
			if(min_xpoint > xpoint)
			  min_xpoint = xpoint;
			if(max_xpoint < xpoint)
			  max_xpoint = xpoint;
			if(min_ypoint > ypoint)
			  min_ypoint = ypoint;
			if(max_ypoint < ypoint)
			  max_ypoint = ypoint;
                        if(NR == 4)
			  current_dataset_color = $4;
			getline;
			if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f left\n", $0, xpoint, secs_2000, ypoint) >> labels_file;
			else printf("set label \"%s\" at %f, %f left\n", $0, xpoint, ypoint) >> labels_file;
			next;
		}


/^go$/		{next}

	{printf("Bad line %d: \"%s\"\n", NR, $0); next;}

# Creating the gnuplot file and deleting all the dataset files after concatenating all contents into one file

END	{
		printf("set title \"%s\"\n", TITLE) >> gpl_file;
		printf("set xlabel \"%s\"\n", XLABEL) >> gpl_file;
		printf("set ylabel \"%s\"\n", YLABEL) >> gpl_file;
		printf("set format x \"%s\"\n", xaxis_format) >> gpl_file;
		printf("set format y \"%s\"\n", yaxis_format) >> gpl_file;
		if(xaxis_type == "timeval" || xaxis_type == "dtime") {
		  printf("set xdata time\n") >> gpl_file;
		}
		printf("set nokey\n") >> gpl_file;
		printf("load \"%s\";\n", labels_file) >> gpl_file;	
		first = 1;
		
		if(entered)
		{
 		for (dataset in dataset_type)
		{
		    
		    FILE=file_name(dataset);
		    if (first)
			printf("plot ") >> gpl_file;
		    else
			printf(", ") >> gpl_file;
		    first = 0;
		    printf("\"%s\" ", FILE) >> gpl_file;

		    if(file_style[dataset] == "dot")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with dots") >> gpl_file;
		        else printf("with dots") >> gpl_file;
			close( FILE );		      
		    }
		    
		    if(file_style[dataset] == "line")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with lines") >> gpl_file;
		        else printf("with lines") >> gpl_file;
			close( FILE );
		    }
		    
		    if(file_style[dataset] == "diamond")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 1") >> gpl_file;
		        else printf("with points pt 1") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "box")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 3") >> gpl_file;
		        else printf("with points pt 3") >> gpl_file;
			close( FILE );
		    }
		
		    if(file_style[dataset] == "cross") 
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 4") >> gpl_file;
			else printf("with points pt 4") >> gpl_file;
			close( FILE );
		    }
		
		    if(file_style[dataset] == "uarrow")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 1") >> gpl_file;
			else printf("with points pt 1") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "darrow")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 1") >> gpl_file;
			else printf("with points pt 1") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "dtick")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "utick")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "x")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 4") >> gpl_file;
			else printf("with points pt 4") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "plus")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
					
		    if(file_style[dataset] == "ltick") 
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "rtick") 
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "htick")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "vtick")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 2") >> gpl_file;
			else printf("with points pt 2") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "larrow")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 5") >> gpl_file;
			else printf("with points pt 5") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "rarrow")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with points pt 5") >> gpl_file;
			else printf("with points pt 5") >> gpl_file;
			close( FILE );
		    }
			
		    if(file_style[dataset] == "dline")
		    {
		        if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("using ($1-946684800.0):2 with linespoints pt 4") >> gpl_file;
			else printf("with linespoints pt 4") >> gpl_file;
			close( FILE );
		    }
			
		}
		for(l=0; l < label_index; l++)
		{
		  xpoint = x_pt[l];
		  ypoint = y_pt[l];
		  if(max_ypoint > 0 && label_dir[l] == -1) ypoint = ypoint - (50000000 * ((max_ypoint - min_ypoint)/max_ypoint));		  
		  if(max_ypoint > 0 && label_dir[l] == +1) ypoint = ypoint + (50000000 * ((max_ypoint - min_ypoint)/max_ypoint));
		  curr_label = label[l];
		  if(xaxis_type == "timeval" || xaxis_type == "dtime") printf("set label \"%s\" at (%f-%f), %f center\n", curr_label, xpoint, secs_2000, ypoint) >> labels_file;
		  else printf("set label \"%s\" at %f, %f center\n", $1, xpoint, ypoint) >> labels_file;

		}
		}
		printf(";\n") >> gpl_file;
		printf("set term postscript\n") >> gpl_file;
		printf("set output \"%s.ps\"\n", BASENAME) >> gpl_file;
		printf("replot\n") >> gpl_file;
		if(labels_present)    printf("load \"%s\";\n", labels_file) >> gpl_file;
		printf("pause -1;\n") >> gpl_file;
		close( gpl_file );

	}	
' $2  # end of AWK

else
  echo "Usage: xpl2gpl [-s] <file_name[.xpl]>" 1>&2;
  exit 1;
fi
