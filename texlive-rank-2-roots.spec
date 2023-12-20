Name:		texlive-rank-2-roots
Version:	68161
Release:	1
Summary:	Draw (mathematical) rank 2 root systems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rank-2-roots
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rank-2-roots.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rank-2-roots.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package concerns mathematical drawings arising in
representation theory. The purpose of this package is to ease
drawing of rank 2 root systems, with Weyl chambers, weight
lattices, and parabolic subgroups. Required packages are tikz,
etoolbox, expl3, pgfkeys, pgfopts, xparse, and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/rank-2-roots
%doc %{_texmfdistdir}/doc/latex/rank-2-roots

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
