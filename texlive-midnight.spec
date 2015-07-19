# revision 15878
# category Package
# catalog-ctan /macros/generic/midnight
# catalog-date 2008-11-09 11:56:27 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-midnight
Version:	20081109
Release:	10
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
%{_texmfdistdir}/tex/generic/midnight/border.tex
%{_texmfdistdir}/tex/generic/midnight/dolines.tex
%{_texmfdistdir}/tex/generic/midnight/gloss.tex
%{_texmfdistdir}/tex/generic/midnight/labels.tex
%{_texmfdistdir}/tex/generic/midnight/loop.tex
%{_texmfdistdir}/tex/generic/midnight/quire.tex
%{_texmfdistdir}/tex/generic/midnight/styledef.tex
%doc %{_texmfdistdir}/doc/generic/midnight/README
%doc %{_texmfdistdir}/doc/generic/midnight/border.doc
%doc %{_texmfdistdir}/doc/generic/midnight/dolines.doc
%doc %{_texmfdistdir}/doc/generic/midnight/gloss.doc
%doc %{_texmfdistdir}/doc/generic/midnight/labels.doc
%doc %{_texmfdistdir}/doc/generic/midnight/loop.doc
%doc %{_texmfdistdir}/doc/generic/midnight/midnight.pdf
%doc %{_texmfdistdir}/doc/generic/midnight/quire.doc
%doc %{_texmfdistdir}/doc/generic/midnight/styledef.doc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081109-2
+ Revision: 753984
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081109-1
+ Revision: 719028
- texlive-midnight
- texlive-midnight
- texlive-midnight
- texlive-midnight

