from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctofitAPITests(APITestCase):

    def test_create_user(self):
        data = {"email": "testuser@example.com", "name": "Test User"}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_team(self):
        user = User.objects.create(email="teamuser@example.com", name="Team User")
        data = {"name": "Team A", "members": [user.id]}
        response = self.client.post("/teams/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_activity(self):
        user = User.objects.create(email="activityuser@example.com", name="Activity User")
        data = {"user": user.id, "type": "Running", "duration": 30, "date": "2025-04-09"}
        response = self.client.post("/activity/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_leaderboard_entry(self):
        user = User.objects.create(email="leaderboarduser@example.com", name="Leaderboard User")
        data = {"user": user.id, "score": 100}
        response = self.client.post("/leaderboard/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_workout(self):
        data = {"name": "Workout A", "description": "Test workout", "duration": 45}
        response = self.client.post("/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
