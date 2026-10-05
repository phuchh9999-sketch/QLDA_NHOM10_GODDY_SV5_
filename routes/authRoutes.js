const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');

router.post('/login', authController.login);
router.post('/register', authController.register);
router.get('/users', authController.getUsers);
router.put('/change-password', authController.changePassword);
router.put('/users/:id/toggle', authController.toggleUserActive);

module.exports = router;