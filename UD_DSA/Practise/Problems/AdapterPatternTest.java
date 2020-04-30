
/**
* So first of all we will have two classes – Volt (to measure volts) and Socket (producing constant volts of 120V).
* This is the voltage class.Here, we have a simple constructor here with the getter and the setter methods. 
* (VOLT CLASS)
*/
class Volt {

	private int volts;
	
	public Volt(int v){
		this.volts=v;
	}

	public int getVolts() {
		return volts;
	}

	public void setVolts(int volts) {
		this.volts = volts;
	}
	
}
/**
* This is the socket class, that basically has the GetVolt method. (SOCKET CLASS)
*/
class Socket {

	public Volt getVolt(){
		return new Volt(120);
	}
}

/**
* This is our Adapter (ADAPTER INTERFACE)
*/
interface SocketAdapter {

	public Volt get120Volt();
		
	public Volt get12Volt();
	
	public Volt get3Volt();
}
/**
* While implementing Adapter pattern, there are two approaches – class adapter and object adapter – however both these approaches produce same result.
* Class Adapter – This form uses java inheritance and extends the source interface, in our case Socket class.
* Object Adapter – This form uses Java Composition and adapter contains the source object.
* Using inheritance for adapter pattern
*/

/**
* This is the Class Adapter,
*/
class SocketClassAdapterImpl extends Socket implements SocketAdapter{

	@Override
	public Volt get120Volt() {
		return getVolt();
	}

	@Override
	public Volt get12Volt() {
		Volt v= getVolt();
		return convertVolt(v,10);
	}

	@Override
	public Volt get3Volt() {
		Volt v= getVolt();
		return convertVolt(v,40);
	}
	
	private Volt convertVolt(Volt v, int i) {
		return new Volt(v.getVolts()/i);
	}

}

/**
* This is the object Adapter
*/

class SocketObjectAdapterImpl implements SocketAdapter{

	//Using Composition for adapter pattern
	private Socket sock = new Socket();
	
	@Override
	public Volt get120Volt() {
		return sock.getVolt();
	}

	@Override
	public Volt get12Volt() {
		Volt v= sock.getVolt();
		return convertVolt(v,10);
	}

	@Override
	public Volt get3Volt() {
		Volt v= sock.getVolt();
		return convertVolt(v,40);
	}
	
	private Volt convertVolt(Volt v, int i) {
		return new Volt(v.getVolts()/i);
	}
}

/**
*  This is the test class that demonstrates both the claass as well as object dapter
*/

public class AdapterPatternTest {

	public static void main(String[] args) {
		
		testClassAdapter();
		testObjectAdapter();
	}
  //This is for the ObjectAdapter(will be printed with object word in the o/p)
	private static void testObjectAdapter() {
		SocketAdapter sockAdapter = new SocketObjectAdapterImpl();
		Volt v3 = getVolt(sockAdapter,3);
		Volt v12 = getVolt(sockAdapter,12);
		Volt v120 = getVolt(sockAdapter,120);
		System.out.println("v3 volts using Object Adapter="+v3.getVolts());
		System.out.println("v12 volts using Object Adapter="+v12.getVolts());
		System.out.println("v120 volts using Object Adapter="+v120.getVolts());
	}
  //This is for the class Adapter(Will be printed with class word in the o/p)
	private static void testClassAdapter() {
		SocketAdapter sockAdapter = new SocketClassAdapterImpl();
		Volt v3 = getVolt(sockAdapter,3);
		Volt v12 = getVolt(sockAdapter,12);
		Volt v120 = getVolt(sockAdapter,120);
		System.out.println("v3 volts using Class Adapter="+v3.getVolts());
		System.out.println("v12 volts using Class Adapter="+v12.getVolts());
		System.out.println("v120 volts using Class Adapter="+v120.getVolts());
	}
	
	private static Volt getVolt(SocketAdapter sockAdapter, int i) {
		switch (i){
		case 3: return sockAdapter.get3Volt();
		case 12: return sockAdapter.get12Volt();
		case 120: return sockAdapter.get120Volt();
		default: return sockAdapter.get120Volt();
		}
	}
}
// ********************************************************OUTPUT********************************************************
/**
*v3 volts using Class Adapter=3
*v12 volts using Class Adapter=12
*v120 volts using Class Adapter=120
*v3 volts using Object Adapter=3
*v12 volts using Object Adapter=12
*v120 volts using Object Adapter=120
*/