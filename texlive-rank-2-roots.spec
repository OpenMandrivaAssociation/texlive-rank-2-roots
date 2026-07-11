%global tl_name rank-2-roots
%global tl_revision 75301

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Draw (mathematical) rank 2 root systems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/rank-2-roots
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rank-2-roots.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rank-2-roots.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package concerns mathematical drawings arising in representation
theory. The purpose of this package is to ease drawing of rank 2 root
systems, with Weyl chambers, weight lattices, and parabolic subgroups.
Required packages are tikz, etoolbox, expl3, pgfkeys, pgfopts, xparse,
and xstring.

