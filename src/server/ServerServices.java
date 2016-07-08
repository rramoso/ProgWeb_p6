package server;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.ws.Endpoint;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Created by ricardoramos on 7/7/16.
 */

@WebService()
public class ServerServices {

    static Map<String, Estudiante> studentsMap = new HashMap<>();
    static List<Asignatura> subjects = new ArrayList<>();

    @WebMethod
    public void crearEstudiante(int id, String name, String career, List<Asignatura> studentSubjects) {
        Estudiante newStudent = new Estudiante(id, name, career);
        newStudent.setSubjects(studentSubjects);
        String stringId = String.valueOf(id);
        studentsMap.put(stringId, newStudent);
    }

    @WebMethod
    public Asignatura getAsignatura(int index) {
        return subjects.get(index);
    }

    @WebMethod
    public List<Asignatura> listAsignatura() {
        return subjects;
    }

    @WebMethod
    public Estudiante getEstudiante(int id) {
        String stringId = String.valueOf(id);
        return studentsMap.get(stringId);
    }

    @WebMethod
    public void updateEstudiante(Estudiante student) {
        String stringId = String.valueOf(student.getId());
        studentsMap.put(stringId, student);
    }

    @WebMethod
    public void removeEstudiante(int id) {
        String stringId = String.valueOf(id);
        studentsMap.remove(stringId);
    }

    @WebMethod
    public List<Estudiante> listEstudiantes() {
        return new ArrayList<Estudiante>(studentsMap.values());
    }

    private static void populateSubjects() {

        subjects.add(new Asignatura("ISC-573", "Tecnologias Emergentes"));
        subjects.add(new Asignatura("ISC-581", "Temas Especiales ISC"));
        subjects.add(new Asignatura("ISC-415", "Programacion Web"));
        subjects.add(new Asignatura("ISC-517", "Programacion Web Avanzada"));
        subjects.add(new Asignatura("ISC-571", "Proyecto Final"));

    }

    public static void main(String[] argv) {
        populateSubjects();
        Object implementor = new ServerServices();
        String address = "http://localhost:8080/ServerService";
        Endpoint.publish(address, implementor);
    }
}
