#! /usr/local/bin/perl
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
################################################################################
# docgen.pl:  
# 
#   docgen reads in an html file generated by the Lumos workshop
#   builds frame html and dumps HTML output
#   in directory where docgen was invoked.  docgen is going to create
#   some html pages in the directory where you invoked it.  For all
#   the HTML files to work together you must have all the HTML files
#   created by docgen in a single directory with the HTML file that Lumos
#   generated.
#
#   usage:
#   /path/to/docgen.pl fileName.html.
#
#   You can also do:
#   docgen.pl /full/path/to/file/fileName.html
#
################################################################################

###############
# SUBROUTINES #
###############

sub page_footer
{
	return <<"end-of-page";
<BR>
<HR>
Copyright &copy; 2001, Calix Networks, Inc. - <b>Proprietary and Confidential Information</b>
<BR>
</BODY>
</HTML>
end-of-page
}

# same as above with no copyright
sub page_foot
{
	return <<"end-of-page";
</body>
</html>
end-of-page
}

sub page_header 
{
	local($titl) = @_;
	return <<"pageTop" 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<html>

<head>
<title>C7 TL1 Documentation</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<link rel="stylesheet" type="text/css" href="stylesheet.css" title="Style">
</head>

<body style="{bgcolor='#FFFFFF'}">

pageTop
}

sub ParseFile 
{	
	local($docName) = shift(@ARGV);
	#print "docname $docName\n";
	# check if input file is there
	if ($docName eq "" ) 
		{
		$docName = "C7Tl1.html";	
		}
	if ( ! -e $docName) 
		{
		print "Unable to find $docName\n";
		return();
		}	
	# now try to open it
	unless(open(INPUT, $docName)) 
		{
		print "Error: cannot open \"$docName\"\n";
		return();
		}	
	
	############################################################################
	$gotTitle    = 0; $gotContents = 0; $gotContact  = 0;		
	$gotDate     = 0; $gotDesc     = 0; $gotVersion  = 0;
		
	# keep track of where we're at in the doc for multi-line sections
	$inCommandCategoriesSection  = 0;
	$inCommandDescriptionSection = 0;
	$inCommandCategory    = 0;
	$inCommandDescription = 0;	
	$inAidSection = 0; $inParamTypes = 0;	
	$inErrors     = 0; $DefaultErrors = 0; $ErrorCodes    = 0;		
	
	############################################################################
	# set of variables for which values are collected as INPUT is parsed
	$docDate = ""; $docVersion = ""; $categoryHeading = "";		
	%categoryHash;
    #$nberOfCategories = 0;
    $nberOfCommands    = 0; $nberOfAids        = 0;    
    @CmdsArr = (); @AidsArr = ();
	# file names 
	$categFile = "categories.html"; $cmdsFile = "athruz.html";
	$aidFile = "aids.html"; $errFile = "errors.html";    

	# top of the page  - a lot of unused stuff currently
	while(<INPUT>) 
		{
        $line = $_;
		#if($line =~ /^<TITLE>/) {
		#	$gotTitle = 1;
		#} elsif($line =~ /^<H2>Contents<\/H2>/) {
		#	$gotContents = 1;
		#} elsif($line =~ /^<H2>Contact<\/H2>/) {
		#	$gotContact = 1;
		#} elsif($line =~ /^<H3>[a-zA-Z]+ 2001<\/H3>/) {

		if($line =~ /^<H3>[a-zA-Z]+ 2001<\/H3>/) 
			{	
			$gotDate = 1;
			$docDate = $line;
			$docDate =~ s/<H3>//;
			$docDate =~ s/<\/H3>//;
			#print "date: $docDate\n";
			} elsif($line =~ /^<H3>Description<\/H3>/) {
			$gotDesc = 1;
			} elsif($line =~ /^<H3>Version<\/H3>/) {
			$gotVersion = 1;			
			} else {
			last if /^<BLOCKQUOTE>/ && $gotVersion;			
			}
		}

    ############################################################################	
	# now we should be on the line with the version number  
    $docVersion = <INPUT>;
	# see if it looks like a version string
    #if ($docVersion =~ /^V/) 
    #	{
	#    $docVersion =~ s/<P>//;
	#    $docVersion =~ s/V//;
	#    $gotVersion = 1;
    #	}
    #print "version: $docVersion\n";
	# if the version is not in the file see if it's in the file name

    #if(!$gotVersion) 
    #	{
    #	if ($docName =~ /_V/) 
    #		{
    #		($throw, $docVersion) = split( /Commands_/, $docName);
    #		$docVersion =~ s/\.html//;
    #		$docVersion =~ s/_/\./g;
    #		$docVersion =~ s/V//;
    #		#print "version: $docVersion\n";
    #		}
    #	}
    
    $nada = <INPUT>;
    ############################################################################
	# start of command categories
    #if ($nada =~ /^<BLOCKQUOTE>/) {
		# the next line is going to be the start 
    	# of the commands categories section
		#$inCommandCategoriesSection = 1;
    #}
    
    while(<INPUT>) 
    	{
    	$line = $_;
    	if ($line =~/^<H2>/) 
    		{
			# at the beginning of category
			# grab heading 
			#$inCommandCategory = 1; 
			$categoryHeading = $line;
			$categoryHeading =~ s/<H2>//;
			$categoryHeading =~ s/<\/H2>//;
			#print "heading $categoryHeading\n";
   		
    		} elsif($line =~ /^<A HREF=/) {
    		$categoryHash{$categoryHeading} .= $line;
    		
    		#} elsif($line =~ /^<\/BLOCKQUOTE>/) {
    		#	$inCommandCategory = 0;
    		} else {
    		last if /^<BR><BR><HR><BR>/ ; 
    		}
    	}
    #$inCommandCategoriesSection = 1;

    $nada = <INPUT>;
    #print "nada $nada\n";    
    ############################################################################
	# start of command descriptions    
    #if ($nada =~ /^<CENTER>/) {
		# the next line is going to be the start 
    	# of the commands description section
		#$inCommandDescriptionSection = 1;
    #}
    
    while(<INPUT>) 
    	{
    	$line = $_;
    	if ($line =~/^<A NAME/) 
    		{
			# at the beginning of command descript.
			# grab command name 
			#$inCommandDescription = 1; 
			$commandName = $line;
			($throw, $commandName) = split( /<H1>/, $commandName);
			$commandName =~ s/<\/H1><\/A>//; 
			$commandName =~ s/\n//g;	
			$commandName =~ s/\r//g;
            $commandName =~ s/\s/%20/g;
			#print "cmd name $commandName\n";
			push(@CmdsArr,$commandName);
			$nberOfCommands++;
    		} else {
    		last if /^<H3><A NAME="aids">/ ; 
    		}
    	}
    #$inCommandDescriptionSection = 0;

    $nada = <INPUT>;
    #print "nada $nada\n";    
    ############################################################################
	# start of AIDs section
    while(<INPUT>) 
    	{
    	$line = $_;
    	if ($line =~/^<H4><A NAME=/) 
    		{
			# at the beginning of AID descript.
			# grab AID name 
			#$inAidSection = 1; 
			$aidName = $line;
			($throw, $aidName) = split( /<H4><A NAME="/, $aidName);
			($aidName, $throw) = split( /"/, $aidName); 
			#print "aid name $aidName\n";
			push(@AidsArr,$aidName);
			$nberOfAids++;
    		} else {
    		last if /^<BR><BR><HR><BR>/ ; 
    		}
    	}
    #$inAidSection = 0;
    
	# for now we skip the Parameter Types section
	# ang go straight to the error section
    while(<INPUT>) 
    	{
    	last if /^<H3><A NAME="errors">/;
    	}
    
    #$nada = <INPUT>;
    #print "nada $nada\n"; 
    
    ############################################################################
	# start of Errors section 
    #$inErrors = 1;
	while(<INPUT>) 
		{
    	$line = $_;
    	if ($line =~ /^<H4><A NAME="Default Errors">Default Errors<\/A><\/H4>/) 
    		{
			# at the beginning of default errors for now just make a note of it			 			 
			$DefaultErrors = 1;
    		} elsif ($line =~ /<H4>Errors<\/H4>/) {
    		# at the beginning of error codes for now just make a note of it
    		$ErrorCodes    = 1;
    		} else { 
    			last if /^<BLOCKQUOTE>/ ; 
    		}
    	}
    #$inErrors = 0;
    
    close INPUT;
    
    ############################################################################
	# done parsing now output HTML pages
    ############################################################################    
    ############################################################################        
    ############################################################################    
	# write out the categories html file
    open(CATEG, ">$categFile") || die "Can't create $categFile\n";
    
	# first dump all the categories into a single categories page
    print CATEG &page_header("Categories");       	    
    print CATEG "<h3>All Categories</h3>\n";
    print CATEG "<table border=\"0\" width=\"100%\">\n<tr>\n<td nowrap>";    
    foreach $category (sort keys(%categoryHash)) 
    	{
		# compose file name
		$tgt = $category;
		chomp($category);
		$tgt =~ s/\)//;    		
		$tgt =~ s/\(//;
		$tgt =~ s/ /_/;
		$tgt =~ s/\n//;	
		$tgt =~ s/\r//;
		$tgt =~ s/\s//;
		#$fileName = "$tgt" . ".html";
		$clean = $category;
		$clean =~ s/\n//g;	
		$clean =~ s/\r//g;		
        if ($clean eq "Fault") {
            print CATEG "<a href=\"$tgt.html\" target=\"tocFrame\" class=\"FrameItemFont\"><b>$clean (Alarms)</b></a>\n<br>\n";
        } else {
            print CATEG "<a href=\"$tgt.html\" target=\"tocFrame\" class=\"FrameItemFont\"><b>$clean</b></a>\n<br>\n";
        }
    	}    
    print CATEG "</td>\n</tr>\n</table>\n";
    print CATEG &page_foot;    
    close CATEG;
    
	# do it again so that the toc-frame has something in it
    open (TOCFRM, ">toc-frame.html")  || die "Can't create toc-frame.html\n";
	# first dump all the categories into a single categories page
    print TOCFRM &page_header("Categories");
    print TOCFRM "<h3>All Categories</h3>\n";
    print TOCFRM "<table border=\"0\" width=\"100%\">\n<tr>\n<td nowrap>";    
    foreach $category (sort keys(%categoryHash)) 
    	{
		# compose file name
		$tgt = $category;
		chomp($category);
		$tgt =~ s/\)//;    		
		$tgt =~ s/\(//;
		$tgt =~ s/ /_/;
		$tgt =~ s/\n//;
		$tgt =~ s/\r//;
		$tgt =~ s/\s//;
		#$fileName = "$tgt" . ".html";
		$clean = $category;
		$clean =~ s/\n//g;	
		$clean =~ s/\r//g;		
        if ($clean eq "Fault") {
            print TOCFRM "<a href=\"$tgt.html\" target=\"tocFrame\" class=\"FrameItemFont\"><b>$clean (Alarms)</b></a>\n<br>\n";
        } else {
            print TOCFRM "<a href=\"$tgt.html\" target=\"tocFrame\" class=\"FrameItemFont\"><b>$clean</b></a>\n<br>\n";
        }
    	}    
    print TOCFRM "</td>\n</tr>\n</table>\n";
    print TOCFRM &page_foot;    
    close TOCFRM;
        
    # now create a page for each category and associated commands
	foreach $category (sort keys(%categoryHash)) 
		{
		# compose file name
		$tgt = $category;		
		$tgt =~ s/\)//;    		
		$tgt =~ s/\(//;
		$tgt =~ s/ /_/;
		$tgt =~ s/\n//;	
		$tgt =~ s/\r//;
		$tgt =~ s/\s//;
		$fileName = "$tgt" . ".html";
		$categName = $category;
		chomp($categName);
	    open(OUTF, ">$fileName") || die "Can't create $fileName\n";
    	print OUTF &page_header($categName);
    	print OUTF "<h3><a href=\"categories.html\" target=\"tocFrame\">Back to categories</a></h3>\n";
    	print OUTF "<h3>$categName</h3>\n";
    	print OUTF "<table border=\"0\" width=\"100%\">\n<tr>\n<td nowrap>";  									
		
    	@cmds = split( /\n/, $categoryHash{$category} );
		
    	foreach $cmd ( @cmds ) 
    		{
    		#print "cmd $cmd\n";
   			$targLink = $cmd;
    		$targLink =~ s/">/\" target=\"contentFrame\" class=\"FrameItemFont\">/;
    		print OUTF "$targLink\n";
			}
	    print OUTF "</td>\n</tr>\n</table>\n";
	    print OUTF &page_foot;    
	    close OUTF;		
		}
	
  
    ############################################################################

    ############################################################################    
	# write out the Commands A-Z html file
    open(ATOZ, ">$cmdsFile") || die "Can't create $cmdsFile\n";
    
	# dump out html header  - title is never seen
    print ATOZ &page_header("Commands A-Z");
    
	# write out each anchor followed by corresponding list of commands
    print ATOZ "<h3><a name=\"top_athruz\">Commands and messages A-Z</a> \
		<br><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#a_ref\">A-C</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#d_ref\">D</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#e_ref\">E</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#i_ref\">I</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#m_ref\">M</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#o_ref\">O-P</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#r_ref\">R</a><br> \
		&nbsp;&nbsp;<a href=\"$cmdsFile#s_ref\">S-Z</a><br> \
		</h3>\n";


	my %map = (
		"A - C" => "a_ref",  
		"D"     => "d_ref",
		"E"     => "e_ref",
		"I"     => "i_ref",
		"M"     => "m_ref",
		"O - P" => "o_ref",  
		"R"     => "r_ref",
		"S - Z" => "s_ref"
		);

	foreach my $key (sort(keys(%map)))
		{
		my $value = $map{$key};

		print ATOZ "<h3><br><a name=\"$value\">&nbsp;&nbsp;$key&nbsp;&nbsp;&nbsp;&nbsp;</a><a href=\"$cmdsFile#top_athruz\" target=\"tocFrame\">Top</a><br></h3>\n";
		print ATOZ "<table border=\"0\" width=\"100%\">\n<tr>\n<td nowrap=\"nowrap\">\n";

		foreach $cmd ( @CmdsArr ) 
			{
			# massage the href for the command in case it contains < or >
			$cmdLink = $cmd;
			$cmdLink =~ s/\&LT\;/_/;
			$cmdLink =~ s/\&GT\;/_/;
			
			$clean = $cmd;
			$clean =~ s/%20/ /g;
			$clean =~ s/\&LT/\&lt/;
			$clean =~ s/\&GT/\&gt/;

			if ( $value =~ /a_ref/ )
				{
				if ( $cmd =~ /^[ABC]/ ) 
					{    		
					print ATOZ "<a href=\"$docName#$cmdLink\" target=\"contentFrame\" class=\"FrameItemFont\">$clean</a><br>\n\n";
					} 
				}
			elsif ( $value =~ /o_ref/ )
				{
				if ( $cmd =~ /^[OP]/ ) 
					{    		
					print ATOZ "<a href=\"$docName#$cmdLink\" target=\"contentFrame\" class=\"FrameItemFont\">$clean</a><br>\n\n";
					} 
				}
			elsif ( $value =~ /s_ref/ )
				{
				if ( $cmd =~ /^[STUVWXYZ]/ ) 
					{    		
					print ATOZ "<a href=\"$docName#$cmdLink\" target=\"contentFrame\" class=\"FrameItemFont\">$clean</a><br>\n\n";
					} 
				}
			else
				{
				if ( $cmd =~ /^$key/ ) 
					{
					print ATOZ "<a href=\"$docName#$cmdLink\" target=\"contentFrame\" class=\"FrameItemFont\">$clean</a><br>\n\n";
					}
				}
			}

		print ATOZ "</td>\n</tr>\n</table>\n";    
		}

   
    print ATOZ &page_foot;    
    close ATOZ;  
    ############################################################################

    ############################################################################    
	# write out the AIDs html file
    open(AID, ">$aidFile") || die "Can't create $aidFile\n";
    
    print AID &page_header("AIDs");
	print AID "<h3>AIDs</h3>\n";
    print AID "<table border=\"0\" width=\"100%\">\n<tr>\n<td nowrap>";       
    # iterate through the array 
    $counter = 0;
    
    foreach $aid ( @AidsArr ) 
    	{
    	print AID "<a href=\"$docName#$aid\"  target=\"contentFrame\" class=\"FrameItemFont\" >$aid</a>\n<br>\n";
    	}
   
    print AID "</td>\n</tr>\n</table>\n";
    print AID &page_foot;    
    close AID;    
    ############################################################################

    ############################################################################    
	# write out the errors html file
    open(ERRF, ">$errFile") || die "Can't create $errFile\n";
    
	# dump out html header  - title is never seen
    print ERRF &page_header("Errors");
    print ERRF "<h3>Error codes & messages</h3>\n";
    if (DefaultErrors) 
    	{ 
    	print ERRF "<a href=\"$docName#errors\"target=\"contentFrame\">Error messages</a>"; 
    	}
    
    print ERRF &page_foot;    
    close ERRF;  
    ############################################################################

    # now take out reference to Lumos at bottom of C7Tl1.html
    $newfile = "C7Tl1.new";
    $file    = "C7Tl1.html";

    $now = localtime(time());
    ($one, $two, $three) = split(/:/, $now);
    ($secnds, $thisYear) = split(/ /, $three);
    
    open(FILE, $file) || die "Can't open $file\n";
    open(OUT, ">$newfile") || die "Can't open $newfile\n";
    @original_file = <FILE>;
    close(FILE);

    for ($i = 0; $original_file[$i]; $i++) {
        # <FONT SIZE=-3>Generated Tue Jun 18 16:24:51 PDT 2002 by the <a href="http://www.lumos.com">Lumos</a> TL1 Workshop 2001.</FONT>
        if ($original_file[$i] =~ /<FONT SIZE=\-3>Generated/) {
	        $original_file[$i] =~ s/ by the <a href=\"http:\/\/www.lumos.com\">Lumos<\/a> TL1 Workshop 200\d//;
            print OUT $original_file[$i]; 
        } else {
           print OUT $original_file[$i];
        }
    }
    
    close(OUT);
    
    if (!rename($newfile,$file)) {
        print "Couldn't rename $newfile to $file\n";
    }
          
}

###########
# PROGRAM #
###########
&ParseFile();
exit(0);

#eof
