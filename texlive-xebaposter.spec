Name:		texlive-xebaposter
Version:	63513
Release:	2
Summary:	Create beautiful scientific Persian/Latin posters using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xebaposter
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xebaposter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xebaposter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed for making beautiful scientific
Persian/Latin posters. It is a fork of baposter by Brian Amberg
and Reinhold Kainhofer available at
http://www.brian-amberg.de/uni/poster/. baposter's users should
be able to compile their poster using xebaposter (instead of
baposter) without any problem.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xebaposter
%doc %{_texmfdistdir}/doc/latex/xebaposter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
