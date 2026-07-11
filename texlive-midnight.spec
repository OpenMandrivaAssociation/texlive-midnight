%global tl_name midnight
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A set of useful macro tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/midnight
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/midnight.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/midnight.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Included are: quire: making booklets, etc.; gloss: vertically align
words in consecutive sentences; loop: a looping construct; dolines:
'meta'-macros to separate arguments by newlines; labels: address labels
and bulk mail letters; styledef: selectively input part of a file; and
border: borders around boxes.

