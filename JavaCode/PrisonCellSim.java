public class PRESO
{
    // instance variables - replace the example below with your own
    public int ID;
    public String name;
    public String surname;
    public int age;
    public int type;
    private String crime;
    private int condena;
    public boolean aislamiento;
    public boolean working;
    public int anch;
    public int prof;
    public int alt;
    public int wnd;
    public double area;
    public boolean chair;

    /**
     * Constructor for objects of class PRESO
     */
    public PRESO(int ID, String name, String surname, int age, int type, String crime, int condena, boolean aislamiento, boolean working)
    {
        // initialise instance variables
        this.ID = ID;
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.type = type;
        this.crime = crime;
        this.condena = condena;
        this.aislamiento = aislamiento;
        this.working = working;
    }
    // Sección de especificación de los datos del preso (métodos set)
    public void setID(int ID)
    {
        this.ID = ID;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    public void setSurname(String surname)
    {
        this.surname = surname;
    }
    public void setAge(int age)
    {
        this.age = age;
    }
    public void setType(int type)
    {
        while(type!=1 && type!=2 && type!=3)
        {
           System.out.println("Solo existen 3 categorias, del uno al tres");
           System.out.println("Siendo el 1 la de menor riesgo y el 3 la de mayor");
           this.type = type;
        }
    }
    public void setCrime(String crime)
    {
        this.crime = crime;
    }
    public void setCondena(int condena)
    {
        this.condena = condena;
    }
    public void setAislamiento(boolean aislamiento)
    {
        this.aislamiento = aislamiento;
    }
    public void setWorking(boolean working)
    {
        this.working = working;
    }
    //Devolución de los datos (métodos get)
    public int getID()
    {
        return ID;
    }
    public String getName()
    {
        return name;
    }
    public String getSurname()
    {
        return surname;
    }
    public int getAge()
    {
        return age;
    }
    public int getType()
    {
        return type;
    }
    public void Riesgo()
    {
        switch(type)
        {
            case 1:
                System.out.println("Preso de bajo riesgo");
                break;
            case 2:
                System.out.println("Preso de riesgo moderado");
                break;
            case 3:
                System.out.println("Preso de alto riesgo");
                break;
        }
    }
    public String getCrime()
    {
        return crime;
    }
    public int getCondena()
    {
        return condena;
    }
    public boolean getAislamiento()
    {
        return aislamiento;
    }
    public void isAislamiento()
    {
        if(aislamiento)
        {
            System.out.println(name + " está en régimen de aislamiento!");
        }
        else
        {
            System.out.println(name + " no está en régimen de aislamiento");
        }
    }
    public boolean getWorking()
    {
        return working;
    }
    public void isWorking()
    {
        if(working)
        {
            System.out.println(name + " está realizando trabajos en la prisión");            
        }
        else
        {
            System.out.println(name + " no está realizando trabajos en la prisión");
        }
    }
    //Con los datos introducidos se creará una celda específica en función de esos datos
    public void makeCell()
    {
        anch = 3;
        prof = 3;
        alt = 2;
        wnd = 0;
        area = 0;
        chair = false;
        if(aislamiento)
        {
            anch = 2;
            prof = 2;
        }
        else
        {
            switch(type)
            {
                case 1:
                    anch = anch + 2;
                    prof = prof + 2;
                    alt = alt + 1;
                    wnd = 2;
                    break;
                case 2:
                    anch = anch + 1;
                    prof = prof + 1;
                    wnd = 1;
                    break;
                case 3:
                    anch = anch + 1;
                    break;
            }
        }
        if(working)
        {
            chair = true;
        }
        else
        {
            chair = false;
        }
        if(age >= 50)
        {
            wnd = wnd + 1;
            chair = true;
        }
        else
        {
        }
        //Si el preso es de alto riesgo la celda será triangular
        if(type != 3)
        {
            area = anch * prof * alt;
        }
        else
        {
            area = (anch * prof * alt)/1.7;
        }
        //Se imprimen los resultados
        System.out.println("El preso nº" + ID + " | " + name + " " + surname + " | tiene una celda cuya área es de: " + area + " metros^2.");
        if(wnd == 0)
        {
            System.out.println("La celda no tiene ventanas.");
        }
        else
        {
            System.out.println("La celda tiene " + wnd + " ventanas.");
        }
        if(chair)
        {
            System.out.println("La celda cuenta con una silla.");
        }
        else
        {
            System.out.println("La celda no tiene silla.");
        }
    }
}
