Summary:	Map client displaying a 3D model of the world
Name:		earth3d
Version:	1.0.5
Release:	0.1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/earth3d/%{name}_client-%{version}-src.tar.bz2
# Source0-md5:	d273437a473f66401b01acf7521808c3
Patch0:		gcc.patch
Patch1:		libpng.patch
URL:		http://www.earth3d.org/
BuildRequires:	ImageMagick-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The map data is fetched from a server on the net, and the client will
display recent satellite images and map data.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
export QTDIR=/usr
qmake earth3d.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# The qmake install target is empty.  Do the install here instead.
install -p earth3d $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
