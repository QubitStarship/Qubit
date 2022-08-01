// Copyright Epic Games, Inc. All Rights Reserved.

#include "TestFPSGameMode.h"
#include "TestFPSCharacter.h"
#include "UObject/ConstructorHelpers.h"

ATestFPSGameMode::ATestFPSGameMode()
	: Super()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnClassFinder(TEXT("/Game/FirstPerson/Blueprints/BP_FirstPersonCharacter"));
	DefaultPawnClass = PlayerPawnClassFinder.Class;

}
