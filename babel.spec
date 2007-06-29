%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           babel
Version:        0.8
Release:        2%{?dist}
Summary:        Tools for internationalizing Python applications

Group:          Development/Languages
License:        BSD
URL:            http://babel.edgewall.org/
Source0:        http://ftp.edgewall.com/pub/babel/Babel-%{version}.tar.bz2
# Upstream patch:
# http://babel.edgewall.org/changeset/192?format=diff&new=192
Patch0:         babel-0.8-pybabel.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-babel

%description
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%package -n python-babel
Summary:        Library for internationalizing Python applications
Group:          Development/Languages

%description -n python-babel
Babel is composed of two major parts:

* tools to build and work with gettext message catalogs

* a Python interface to the CLDR (Common Locale Data Repository),
  providing access to various locale display names, localized number
  and date formatting, etc.

%prep
%setup0 -q -n Babel-%{version}
%patch0 -p1
chmod a-x babel/messages/frontend.py doc/logo.png doc/logo_small.png
%{__sed} -i -e '/^#!/,1d' babel/messages/frontend.py

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README.txt doc/cmdline.txt
%{_bindir}/pybabel

%files -n python-babel
%defattr(-,root,root,-)
%doc doc
%{python_sitelib}/*

%changelog
* Fri Jun 29 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.8-2
- Apply upstream patch to rename command line script to "pybabel" - BZ#246208

* Thu Jun 21 2007 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.8-1
- First version for Fedora

