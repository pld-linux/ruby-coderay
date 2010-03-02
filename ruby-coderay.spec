%define pkgname coderay
Summary:	Ruby library for syntax highlighting
Name:		ruby-%{pkgname}
Version:	0.9.1
Release:	1
License:	LGPL
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d6049cfb54b0702d7a40e59b37f74933
Group:		Development/Languages
URL:		http://coderay.rubychan.de/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
CodeRay is a Ruby library for syntax highlighting.
I try to make CodeRay easy to use and intuitive,
but at the same time fully featured, complete, fast and
efficient. Usage is simple: CodeRay.scan(code, :ruby).div 

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer FOLDERS -o -print | xargs touch --reference %{SOURCE0}

%{__sed} -i -e 's|/usr/bin/env ruby|%{__ruby}|' bin/coderay*

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{GZip,String,Term}
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/coderay* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FOLDERS lib/README
%attr(755,root,root) %{_bindir}/coderay
%attr(755,root,root) %{_bindir}/coderay_stylesheet
%{ruby_rubylibdir}/%{pkgname}.rb
%{ruby_rubylibdir}/%{pkgname}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/CodeRay
