from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Income, Expense, Budget
from .forms import IncomeForm, ExpenseForm, BudgetForm

# Register view
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("dashboard")
    return render(request, "register.html")

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")

# Dashboard view
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    budgets = Budget.objects.filter(user=request.user)

    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    remaining_savings = total_income - total_expense
    num_expenses = expenses.count()

    report = {
        "total_income": total_income,
        "total_expense": total_expense,
        "remaining_savings": remaining_savings,
        "number_of_expenses": num_expenses,
    }

    context = {
        "incomes": incomes,
        "expenses": expenses,
        "budgets": budgets,
        "report": report,
    }
    return render(request, "dashboard.html", context)

# Create Income view
def income_create(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect("dashboard")
    else:
        form = IncomeForm()
    return render(request, "income_form.html", {"form": form})

# Create Expense view
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm()
    return render(request, "expense_form.html", {"form": form})

# Create Budget view
def budget_create(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect("dashboard")
    else:
        form = BudgetForm()
    return render(request, "budget_form.html", {"form": form})
