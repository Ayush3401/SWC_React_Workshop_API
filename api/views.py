from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def AnimeCharacters(request):
    characters = [
        {
            'name': 'Lelouch Lamperouge',
            'image': 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/09/Code-Geass-Lelouch-Lamperouge-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Code Geass'
        },
        {
            'name': 'L Lawliet',
            'image': 'https://static0.cbrimages.com/wordpress/wp-content/uploads/2019/09/Death-Note-L-Lawliet-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Death Note'
        },
        {
            'name': 'Monkey D. Luffy',
            'image': 'https://static0.cbrimages.com/wordpress/wp-content/uploads/2019/09/One-Piece-Monkey-D.-Luffy-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'One Piece'
        },
        {
            'name': 'Levi Ackerman',
            'image': 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/09/Attack-on-Titan-Levi-Ackerman-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Attack On Titan'
        },
        {
            'name': 'Edward Elric',
            'image': 'https://static3.cbrimages.com/wordpress/wp-content/uploads/2019/09/Fullmetal-Alchemist-Edward-Elric-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Fullmetal Alchemist'
        },
        {
            'name': 'Light Yagami',
            'image': 'https://static0.cbrimages.com/wordpress/wp-content/uploads/2019/09/Death-Note-Light-Yagami-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Death Note'
        },
        {
            'name': 'Rintarou Okabe',
            'image': 'https://static0.cbrimages.com/wordpress/wp-content/uploads/2019/09/Steins-Gate-Rintarou-Okabe-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Steings;Gate'
        },
        {
            'name': 'Roronoa Zoro',
            'image': 'https://static1.cbrimages.com/wordpress/wp-content/uploads/2019/09/One-Piece-Roronoa-Zoro-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'One Piece'
        },
        {
            'name': 'Naruto Uzamaki',
            'image': 'https://static3.cbrimages.com/wordpress/wp-content/uploads/2019/09/Naruto-Naruto-Uzumaki-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Naruto'
        },
        {
            'name': 'Sakata Gintoki',
            'image': 'https://static3.cbrimages.com/wordpress/wp-content/uploads/2019/09/Gintama-Sakata-Gintoki-Cropped.jpg?q=50&fit=crop&w=740&h=370&dpr=1.5',
            'anime': 'Gintama'
        }
    ]
    return Response(characters)
