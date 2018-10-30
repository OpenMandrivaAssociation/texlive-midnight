Name:		texlive-midnight
Version:	20180303
Release:	2
Summary:	A set of useful macro tools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/midnight
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midnight.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midnight.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Included are: - quire: making booklets, etc.; - gloss:
vertically align words in consecutive sentences; - loop: a
looping construct; - dolines: 'meta'-macros to separate
arguments by newlines; - labels: address labels and bulk mail
letters; - styledef: selectively input part of a file; and -
border: borders around boxes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/midnight
%doc %{_texmfdistdir}/doc/generic/midnight

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
