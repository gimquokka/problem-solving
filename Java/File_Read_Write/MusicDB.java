import java.io.*;
import java.util.*;

// 한 노래 정보 저장하는 Song 클래스
class Song implements Comparable<Song> {
    String title;
    String artist;
    String album;
    String track;

    // Comparable 클래스 메소드를 구현
    public int compareTo(Song otherSong) {
        return this.title.compareTo(otherSong.title); // 노래 제목 순으로 노래목록을 정렬
    }

    // 생성자
    Song(String t, String a, String al, String tr) {
        title = t;
        artist = a;
        album = al;
        track = tr;
    }

    public String getTitle() {
        return title;
    }

    public String getArtist() {
        return artist;
    }

    public String getAlbum() {
        return album;
    }

    public String getTrack() {
        return track;
    }

    // Song 클래스 정보를 문자열로 리턴하는 메소드
    @Override
    public String toString() {
        return title+":"+artist+":"+album+":"+track;
    }
}

public class MusicDB {
    // Song 클래스를 인자로하는 컬렉션 ArrayList 생성
    List<Song> songs = new ArrayList<>();

    public static void main(String[] args) {
        new MusicDB().start();
    }

    public void start() {
        // ArrayList의 요소를 파일로부터 읽어옴
        getSongs();
        // ArrayList의 요소를 노래 제목 순으로 정렬하도록 Collections 클래스 메소드 호출
        Collections.sort(songs);
        // 정렬된 ArrayList의 요소를 새 파일에 저장함
        putSongs();
    }


    void getSongs() {
        // 읽을 원본 파일
        // replace pathname to absolute-path where you want
        File inFile = new File("/Users/jin/Desktop/2021-Spring/OOP/HW/OOP_HW4/src/main/java/MusicSrcList.txt");

        try {
            // 파일 입력 문자 스트림에 연결하고, 다시 버퍼 입력 스트림에 연결
            BufferedReader reader = new BufferedReader(new FileReader(inFile));
            String line = null;
            while ((line = reader.readLine()) != null) {
                // 한 줄씩 읽어서 Song 클래스에 저장하는 메소드 호출
                addSong(line);
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    void putSongs() {
        // 저장할 파일
        // replace pathname to absolute-path where you want
        File outFile = new File("/Users/jin/Desktop/2021-Spring/OOP/HW/OOP_HW4/src/main/java/MusicDstList.txt");
        try {
            // 파일 출력 문자 스트림에 연결하고, 다시 버퍼 출력 스트림에 연결
            BufferedWriter writer = new BufferedWriter(new FileWriter(outFile));
            // ArrayList의 요소를 순서대로 접근하기 위해 Interator 객체 생성
            Iterator<Song> it = songs.iterator();
            while (it.hasNext()) {
                // ArrayList의 한 요소를 파일에 저장
                writer.write(it.next().toString()+"\r\n");
            }
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 문자열을 ":"로 구분하여 Song 클래스 객체에 저장후 컬렉션에 삽입하는 메소드
    void addSong(String lineToParse) {
        // 문자열을 ":"로 구분하여 분리
        String[] tokens = lineToParse.split(":");
        // Song 클래스 객체를 생성하여 문자열을 저장
        Song nextSong = new Song(tokens[0], tokens[1], tokens[2], tokens[3]);
        // Song 클래스를 컬렉션에 삽입
        songs.add(nextSong);
    }
}
