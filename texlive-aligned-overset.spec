%global tl_name aligned-overset
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.0
Release:	%{tl_revision}.1
Summary:	Fix alignment at \overset or \underset
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aligned-overset
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aligned-overset.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the base character of \underset or \overset to be
used as the alignment position for the amsmath aligned math
environments.

