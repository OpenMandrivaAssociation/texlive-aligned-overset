Name:		texlive-aligned-overset
Version:	47290
Release:	2
Summary:	Fix alignment at \overset or \underset
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aligned-overset
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows the base character of \underset or \overset
to be used as the alignment position for the amsmath aligned
math environments.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/aligned-overset
%{_texmfdistdir}/tex/latex/aligned-overset
%doc %{_texmfdistdir}/doc/latex/aligned-overset

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
