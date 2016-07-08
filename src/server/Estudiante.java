package server;

import java.util.List;

/**
 * Created by ricardoramos on 7/7/16.
 */
public class Estudiante {

    private int matricula;
    private String nombre;
    private String carrera;
    private List<Asignatura> materias;

    public Estudiante() { }

    public Estudiante(int matricula, String nombre, String carrera) {
        this.matricula = matricula;
        this.nombre = nombre;
        this.carrera = carrera;
    }

    public int getId() {
        return matricula;
    }

    public void setId(int matricula) {
        this.matricula = matricula;
    }

    public String getName() {
        return nombre;
    }

    public void setName(String name) {
        this.nombre = name;
    }

    public String getCareer() {
        return carrera;
    }

    public void setCareer(String career) {
        this.carrera = career;
    }

    public List<Asignatura> getSubjects() {
        return materias;
    }

    public void setSubjects(List<Asignatura> materias) {
        this.materias = materias;
    }
}
