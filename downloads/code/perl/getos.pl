#!/usr/bin/env perl
use strict;

# https://www.alma.ch/perl/perloses.htm
my $os  =  $^O;

print "Current OS is $os\n";

if($^O eq "MSWin32" or $^O eq "msys"){
    print "Windows";
}elsif($^O eq "linux"){
    print "Linux";
}elsif($^O eq "darwin"){
    print "MacOS";
    # $pvc_view_file_via_temporary = 0;
    # $pdf_previewer = "Skim %O %S";
}
