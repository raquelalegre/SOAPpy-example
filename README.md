# SOAPpy-example

Playing around with SOAPpy. 

If you want to run it you probably need to install SOAPpy first, e.g.: `pip install SOAPpy`.

To run this:

```bash
git clone https://github.com/raquel-ucl/SOAPpy-example.git
cd SOAPpy-example
python client.py wsdl/GoogleSearch.wsdl
python client.py wsdl/weather.wsdl
python client.py wsdl/osc.wsdl
```

Each of those python commands will print out the list of available functionality in each server followed by the list of arguments of a randomly chosen method. Execute several times to maximise the fun.

Also takes a URL to another WSDL file as argument.

Note osc.wsdl doesn't work yet due to "No address binding found in port.", since it assumes I'm running a server in localhost:80 which I'm not. Needs to point to the live ORACC service to work properly.

__Important Note__: SOAPpy is outdated and clumsy and although it works to lists available stuff in a server, it does not work when you try to call the methods in the server. Switching to __[suds](https://fedorahosted.org/suds/wiki/Documentation)__ instead. 
