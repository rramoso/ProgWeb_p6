package server;

/**
 * Created by ricardoramos on 7/7/16.
 */
public class Asignatura {

    private String code;
    private String name;

    public Asignatura() { }

    public Asignatura(String code, String name) {
        this.code = code;
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
