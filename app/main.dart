
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AI Crush Bot 💕',
      theme: ThemeData(
        primaryColor: Colors.pink,
        scaffoldBackgroundColor: Colors.pink[50],
      ),
      home: CharacterSelectionScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class CharacterSelectionScreen extends StatefulWidget {
  @override
  _CharacterSelectionScreenState createState() =>
      _CharacterSelectionScreenState();
}

class _CharacterSelectionScreenState extends State<CharacterSelectionScreen> {
  TextEditingController _nameController = TextEditingController();
  List<String> selectedPersonalities = [];
  String selectedCharacter = 'Girlfriend';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('💖 Choose Your Crush 💖'),
        backgroundColor: Colors.pinkAccent,
        centerTitle: true,
      ),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            Text(
              '✨ Customize Your Dream Crush ✨',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            TextField(
              controller: _nameController,
              decoration: InputDecoration(
                labelText: 'Name your Crush 💕',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
              ),
            ),
            SizedBox(height: 20),
            DropdownButtonFormField(
              decoration: InputDecoration(labelText: 'Select Personality'),
              onChanged: (value) {
                setState(() {
                  if (!selectedPersonalities.contains(value)) {
                    selectedPersonalities.add(value!);
                  }
                });
              },
              items: ['Cute', 'Funny', 'Romantic', 'Caring', 'Sarcastic', 'Supportive', 'Sensitive', 'Mood Swings', 'Cute but Angry']
                  .map((personality) {
                return DropdownMenuItem(
                  value: personality,
                  child: Text(personality),
                );
              }).toList(),
            ),
            SizedBox(height: 20),
            DropdownButton<String>(
              value: selectedCharacter,
              onChanged: (value) {
                setState(() {
                  selectedCharacter = value!;
                });
              },
              items: ['Girlfriend', 'Boyfriend', 'Best Friend']
                  .map((character) {
                return DropdownMenuItem(
                  value: character,
                  child: Text(character),
                );
              }).toList(),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ChatScreen(
                      crushName: _nameController.text,
                      personality: selectedPersonalities.join(","),
                      character: selectedCharacter,
                    ),
                  ),
                );
              },
              child: Text('💌 Start Chat'),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.pink),
            ),
          ],
        ),
      ),
    );
  }
}

class ChatScreen extends StatefulWidget {
  final String crushName;
  final String personality;
  final String character;

  ChatScreen({required this.crushName, required this.personality, required this.character});

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  TextEditingController _controller = TextEditingController();
  List<Map<String, String>> messages = [];

  Future<void> sendMessage(String message) async {
    if (message.isEmpty) return;

    setState(() {
      messages.add({'sender': 'You', 'text': message});
    });

    var url = Uri.parse(
        "http://127.0.0.1:5000/chat?message=$message&personality=${widget.personality}&character=${widget.character}");

    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        var data = json.decode(response.body);
        setState(() {
          messages.add({'sender': widget.crushName, 'text': data['reply']});
        });
      } else {
        setState(() {
          messages.add({'sender': widget.crushName, 'text': 'Oops! Something went wrong 💔'});
        });
      }
    } catch (e) {
      setState(() {
        messages.add({'sender': widget.crushName, 'text': 'Network error 💔'});
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('${widget.crushName} 💕'),
        backgroundColor: Colors.pinkAccent,
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                final message = messages[index];
                return Align(
                  alignment: message['sender'] == 'You'
                      ? Alignment.centerRight
                      : Alignment.centerLeft,
                  child: Container(
                    padding: EdgeInsets.all(12),
                    margin: EdgeInsets.symmetric(vertical: 10),
                    decoration: BoxDecoration(
                      color: message['sender'] == 'You'
                          ? Colors.pink[100]
                          : Colors.pink[300],
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      '${message['sender']}: ${message['text']}',
                      style: TextStyle(color: Colors.white),
                    ),
                  ),
                );
              },
            ),
          ),
          Padding(
            padding: EdgeInsets.all(10),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(hintText: 'Say something 💕'),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send, color: Colors.pink),
                  onPressed: () {
                    sendMessage(_controller.text);
                    _controller.clear();
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
