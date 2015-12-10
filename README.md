# SOAPpy-example

Playing around with SOAPpy. 

To run this:

```bash
git clone https://github.com/raquel-ucl/SOAPpy-example.git
cd SOAPpy-example
python client.py GoogleSearch.wsdl
python client.py weather.wsdl
python client.py osc.wsdl
```

Each of those python commands will print out the list of available functionality in each server followed but the list of arguments of a randomly chosen method.

Note osc.wsdl doesn't work yet due to "No address binding found in port.", since it assumes I'm running a server in localhost:80 which I'm not. Needs to point to the live ORACC service to work properly.
